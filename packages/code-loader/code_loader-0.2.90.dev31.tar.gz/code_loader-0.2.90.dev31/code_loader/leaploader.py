# mypy: ignore-errors
import importlib.util
import io
import sys
from contextlib import redirect_stdout
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Iterable, Union

import numpy as np
import numpy.typing as npt
import tensorflow as tf  # type: ignore

torch_imported = False
try:
    import torch  # type: ignore

    torch_imported = True
except Exception as e:
    print(f"importing torch failed with exception: {repr(e)}")

from code_loader.contract.datasetclasses import DatasetSample, DatasetBaseHandler, InputHandler, \
    GroundTruthHandler, PreprocessResponse, VisualizerHandler, VisualizerCallableReturnType, CustomLossHandler, \
    PredictionTypeHandler, MetadataHandler, CustomLayerHandler, MetricHandler
from code_loader.contract.enums import DataStateEnum, TestingSectionEnum, DataStateType, DatasetMetadataType
from code_loader.contract.exceptions import DatasetScriptException
from code_loader.contract.responsedataclasses import DatasetIntegParseResult, DatasetTestResultPayload, \
    DatasetPreprocess, DatasetSetup, DatasetInputInstance, DatasetOutputInstance, DatasetMetadataInstance, \
    VisualizerInstance, PredictionTypeInstance, ModelSetup, CustomLayerInstance, MetricInstance, CustomLossInstance
from code_loader.leap_binder import global_leap_binder
from code_loader.utils import get_root_exception_line_number, get_shape


class LeapLoader:
    def __init__(self, code_path: str, code_entry_name: str):
        self.code_entry_name = code_entry_name
        self.code_path = code_path

    @lru_cache()
    def exec_script(self) -> None:
        try:
            if torch_imported:
                # disable GPU on torch module
                torch.cuda.is_available = lambda: False

            self.evaluate_module()
        except TypeError as e:
            import traceback
            if "leap_binder.set_metadata(" in traceback.format_exc(5):
                raise DeprecationWarning(
                    "Please remove the metadata_type on leap_binder.set_metadata in your dataset script")
            raise DatasetScriptException(getattr(e, 'message', repr(e))) from e
        except Exception as e:
            raise DatasetScriptException(getattr(e, 'message', repr(e))) from e

    def evaluate_module(self) -> None:
        def append_path_recursively(full_path: str) -> None:
            if '/' not in full_path or full_path == '/':
                return

            parent_path = str(Path(full_path).parent)
            append_path_recursively(parent_path)
            sys.path.append(parent_path)

        file_path = Path(self.code_path, self.code_entry_name)
        append_path_recursively(str(file_path))

        spec = importlib.util.spec_from_file_location(self.code_path, file_path)
        if spec is None or spec.loader is None:
            raise DatasetScriptException(f'Something is went wrong with spec file from: {file_path}')

        file = importlib.util.module_from_spec(spec)
        if file is None:
            raise DatasetScriptException(f'Something is went wrong with import module from: {file_path}')

        spec.loader.exec_module(file)

    @lru_cache()
    def metric_by_name(self) -> Dict[str, MetricHandler]:
        self.exec_script()
        setup = global_leap_binder.setup_container
        return {
            metric_handler.name: metric_handler
            for metric_handler in setup.metrics
        }

    @lru_cache()
    def visualizer_by_name(self) -> Dict[str, VisualizerHandler]:
        self.exec_script()
        setup = global_leap_binder.setup_container
        return {
            visualizer_handler.name: visualizer_handler
            for visualizer_handler in setup.visualizers
        }

    @lru_cache()
    def custom_loss_by_name(self) -> Dict[str, CustomLossHandler]:
        self.exec_script()
        setup = global_leap_binder.setup_container
        return {
            custom_loss_handler.name: custom_loss_handler
            for custom_loss_handler in setup.custom_loss_handlers
        }

    @lru_cache()
    def custom_layers(self) -> Dict[str, CustomLayerHandler]:
        self.exec_script()
        return global_leap_binder.setup_container.custom_layers

    @lru_cache()
    def prediction_type_by_name(self) -> Dict[str, PredictionTypeHandler]:
        self.exec_script()
        setup = global_leap_binder.setup_container
        return {
            prediction_type.name: prediction_type
            for prediction_type in setup.prediction_types
        }

    def get_sample(self, state: DataStateEnum, idx: int) -> DatasetSample:
        with tf.device('/cpu:0'):
            self.exec_script()
            sample = DatasetSample(inputs=self._get_inputs(state, idx),
                                   gt=None if state == DataStateEnum.unlabeled else self._get_gt(state, idx),
                                   metadata=self._get_metadata(state, idx),
                                   index=idx,
                                   state=state)
            return sample

    def check_dataset(self) -> DatasetIntegParseResult:
        test_payloads: List[DatasetTestResultPayload] = []
        setup_response = None
        general_error = None
        stdout_steam = io.StringIO()
        with redirect_stdout(stdout_steam):
            try:
                self.exec_script()
                preprocess_test_payload = self._check_preprocess()
                test_payloads.append(preprocess_test_payload)
                handlers_test_payloads = self._check_handlers()
                test_payloads.extend(handlers_test_payloads)
                is_valid = all([payload.is_passed for payload in test_payloads])
                setup_response = self.get_dataset_setup_response(handlers_test_payloads)
            except DatasetScriptException as e:
                line_number = get_root_exception_line_number()
                general_error = f"Something went wrong, {repr(e.__cause__)} line number: {line_number}"
                is_valid = False
            except Exception as e:
                line_number = get_root_exception_line_number()
                general_error = f"Something went wrong, {repr(e)} line number: {line_number}"
                is_valid = False

        print_log = stdout_steam.getvalue()
        is_valid_for_model = bool(global_leap_binder.setup_container.custom_layers)
        model_setup = self.get_model_setup_response()

        return DatasetIntegParseResult(is_valid=is_valid, payloads=test_payloads,
                                       is_valid_for_model=is_valid_for_model, setup=setup_response,
                                       model_setup=model_setup, general_error=general_error,
                                       print_log=print_log)

    def _check_preprocess(self) -> DatasetTestResultPayload:
        preprocess_handler = global_leap_binder.setup_container.preprocess
        unlabeled_preprocess_handler = global_leap_binder.setup_container.unlabeled_data_preprocess
        test_result = DatasetTestResultPayload('preprocess')
        try:
            if preprocess_handler is None:
                raise Exception('None preprocess_handler')
            preprocess_result = self._preprocess_result()
            for state, preprocess_response in preprocess_result.items():
                if unlabeled_preprocess_handler is not None and state == DataStateEnum.unlabeled:
                    unlabeled_preprocess_handler.data_length = preprocess_response.length
                else:
                    state_type = DataStateType(state.name)
                    preprocess_handler.data_length[state_type] = preprocess_response.length

        except Exception as e:
            line_number = get_root_exception_line_number()
            error_string = f"{repr(e)} line number: {line_number}"
            test_result.display[TestingSectionEnum.Errors.name] = error_string
            test_result.is_passed = False
        return test_result

    def _check_handlers(self) -> List[DatasetTestResultPayload]:
        preprocess_result = self._preprocess_result()
        result_payloads: List[DatasetTestResultPayload] = []
        idx = 0
        dataset_base_handlers: List[Union[DatasetBaseHandler, MetadataHandler]] = self._get_all_dataset_base_handlers()
        for dataset_base_handler in dataset_base_handlers:
            test_result = [DatasetTestResultPayload(dataset_base_handler.name)]
            for state, preprocess_response in preprocess_result.items():
                if state == DataStateEnum.unlabeled and isinstance(dataset_base_handler, GroundTruthHandler):
                    continue
                state_name = state.name
                try:
                    raw_result = dataset_base_handler.function(idx, preprocess_response)
                    handler_type = 'metadata' if isinstance(dataset_base_handler, MetadataHandler) else None
                    if isinstance(dataset_base_handler, MetadataHandler) and isinstance(raw_result, dict):
                        metadata_test_result_payloads = [
                            DatasetTestResultPayload(f'{dataset_base_handler.name}_{single_metadata_name}')
                            for single_metadata_name, single_metadata_result in raw_result.items()
                        ]
                        for i, (single_metadata_name, single_metadata_result) in enumerate(raw_result.items()):
                            metadata_test_result = metadata_test_result_payloads[i]
                            result_shape = get_shape(single_metadata_result)
                            metadata_test_result.shape = result_shape
                            metadata_test_result.raw_result = single_metadata_result
                            metadata_test_result.handler_type = handler_type
                        test_result = metadata_test_result_payloads
                    else:
                        result_shape = get_shape(raw_result)
                        test_result[0].shape = result_shape
                        test_result[0].raw_result = raw_result
                        test_result[0].handler_type = handler_type

                        # setting shape in setup for all encoders
                        if isinstance(dataset_base_handler, (InputHandler, GroundTruthHandler)):
                            dataset_base_handler.shape = result_shape

                except Exception as e:
                    line_number = get_root_exception_line_number()
                    test_result[0].display[state_name] = f"{repr(e)} line number: {line_number}"
                    test_result[0].is_passed = False

            result_payloads.extend(test_result)

        return result_payloads

    @staticmethod
    def _get_all_dataset_base_handlers() -> List[Union[DatasetBaseHandler, MetadataHandler]]:
        all_dataset_base_handlers: List[Union[DatasetBaseHandler, MetadataHandler]] = []
        all_dataset_base_handlers.extend(global_leap_binder.setup_container.inputs)
        all_dataset_base_handlers.extend(global_leap_binder.setup_container.ground_truths)
        all_dataset_base_handlers.extend(global_leap_binder.setup_container.metadata)
        return all_dataset_base_handlers

    def run_visualizer(self, visualizer_name: str, input_tensors_by_arg_name: Dict[str, npt.NDArray[np.float32]],
                       ) -> VisualizerCallableReturnType:
        return self.visualizer_by_name()[visualizer_name].function(**input_tensors_by_arg_name)

    def run_heatmap_visualizer(self, visualizer_name: str, input_tensors_by_arg_name: Dict[str, npt.NDArray[np.float32]]
                               ) -> npt.NDArray[np.float32]:
        heatmap_function = self.visualizer_by_name()[visualizer_name].heatmap_function
        if heatmap_function is None:
            assert len(input_tensors_by_arg_name) == 1
            return list(input_tensors_by_arg_name.values())[0]
        return heatmap_function(**input_tensors_by_arg_name)

    @staticmethod
    def get_dataset_setup_response(handlers_test_payloads: List[DatasetTestResultPayload]) -> DatasetSetup:
        setup = global_leap_binder.setup_container
        assert setup.preprocess is not None

        unlabeled_length = None
        if global_leap_binder.setup_container.unlabeled_data_preprocess:
            unlabeled_length = global_leap_binder.setup_container.unlabeled_data_preprocess.data_length
        dataset_preprocess = DatasetPreprocess(
            training_length=setup.preprocess.data_length[DataStateType.training],
            validation_length=setup.preprocess.data_length[DataStateType.validation],
            test_length=setup.preprocess.data_length.get(DataStateType.test),
            unlabeled_length=unlabeled_length
        )

        inputs = []
        for inp in setup.inputs:
            if inp.shape is None:
                raise Exception(f"cant calculate shape for input, input name:{inp.name}")
            inputs.append(DatasetInputInstance(name=inp.name, shape=inp.shape))

        ground_truths = []
        for gt in setup.ground_truths:
            if gt.shape is None:
                raise Exception(f"cant calculate shape for ground truth, gt name:{gt.name}")
            ground_truths.append(
                DatasetOutputInstance(name=gt.name, shape=gt.shape))

        metadata_instances = []
        for handler_test_payload in handlers_test_payloads:
            if handler_test_payload.handler_type != 'metadata':
                continue
            if hasattr(handler_test_payload.raw_result, 'tolist'):
                handler_test_payload.raw_result = handler_test_payload.raw_result.tolist()
            metadata_type = type(handler_test_payload.raw_result)
            if metadata_type == int:
                metadata_type = float
            if metadata_type == str:
                dataset_metadata_type = DatasetMetadataType.string
            elif metadata_type == bool:
                dataset_metadata_type = DatasetMetadataType.boolean
            elif metadata_type == float:
                dataset_metadata_type = DatasetMetadataType.float
            else:
                raise Exception(f"Unsupported return type of metadata {handler_test_payload.name}."
                                f"The return type should be one of [int, float, str, bool]. Got {metadata_type}")
            metadata_instances.append(DatasetMetadataInstance(name=handler_test_payload.name,
                                                              type=dataset_metadata_type))

        visualizers = [
            VisualizerInstance(visualizer_handler.name, visualizer_handler.type, visualizer_handler.arg_names)
            for visualizer_handler in setup.visualizers]

        custom_losses = [CustomLossInstance(custom_loss.name, custom_loss.arg_names)
                         for custom_loss in setup.custom_loss_handlers]

        prediction_types = []
        for prediction_type in setup.prediction_types:
            pred_type_inst = PredictionTypeInstance(prediction_type.name, prediction_type.labels)
            prediction_types.append(pred_type_inst)

        metrics = []
        for metric in setup.metrics:
            metric_inst = MetricInstance(metric.name, metric.arg_names)
            metrics.append(metric_inst)

        return DatasetSetup(preprocess=dataset_preprocess, inputs=inputs, outputs=ground_truths,
                            metadata=metadata_instances, visualizers=visualizers, prediction_types=prediction_types,
                            custom_losses=custom_losses, metrics=metrics)

    @staticmethod
    def get_model_setup_response() -> ModelSetup:
        setup = global_leap_binder.setup_container
        custom_layer_instances = [
            CustomLayerInstance(custom_layer_handler.name, custom_layer_handler.init_arg_names,
                                custom_layer_handler.call_arg_names)
            for custom_layer_handler in setup.custom_layers.values()
        ]
        return ModelSetup(custom_layer_instances)

    @lru_cache()
    def _preprocess_result(self) -> Dict[DataStateEnum, PreprocessResponse]:
        self.exec_script()
        preprocess = global_leap_binder.setup_container.preprocess
        # TODO: add caching of subset result
        assert preprocess is not None
        preprocess_results = preprocess.function()
        preprocess_result_dict = {
            DataStateEnum(i): preprocess_result
            for i, preprocess_result in enumerate(preprocess_results)
        }

        unlabeled_preprocess = global_leap_binder.setup_container.unlabeled_data_preprocess
        if unlabeled_preprocess is not None:
            preprocess_result_dict[DataStateEnum.unlabeled] = unlabeled_preprocess.function()

        return preprocess_result_dict

    def _get_dataset_handlers(self, handlers: Iterable[DatasetBaseHandler],
                              state: DataStateEnum, idx: int) -> Dict[str, npt.NDArray[np.float32]]:
        result_agg = {}
        preprocess_result = self._preprocess_result()
        preprocess_state = preprocess_result[state]
        for handler in handlers:
            handler_result = handler.function(idx, preprocess_state)
            handler_name = handler.name
            result_agg[handler_name] = handler_result
        return result_agg

    def _get_inputs(self, state: DataStateEnum, idx: int) -> Dict[str, npt.NDArray[np.float32]]:
        return self._get_dataset_handlers(global_leap_binder.setup_container.inputs, state, idx)

    def _get_gt(self, state: DataStateEnum, idx: int) -> Dict[str, npt.NDArray[np.float32]]:
        return self._get_dataset_handlers(global_leap_binder.setup_container.ground_truths, state, idx)

    def _get_metadata(self, state: DataStateEnum, idx: int) -> Dict[str, Union[str, int, bool, float]]:
        result_agg = {}
        preprocess_result = self._preprocess_result()
        preprocess_state = preprocess_result[state]
        for handler in global_leap_binder.setup_container.metadata:
            handler_result = handler.function(idx, preprocess_state)
            if isinstance(handler_result, dict):
                for single_metadata_name, single_metadata_result in handler_result.items():
                    handler_name = f'{handler.name}_{single_metadata_name}'
                    result_agg[handler_name] = single_metadata_result
            else:
                handler_name = handler.name
                result_agg[handler_name] = handler_result

        return result_agg
