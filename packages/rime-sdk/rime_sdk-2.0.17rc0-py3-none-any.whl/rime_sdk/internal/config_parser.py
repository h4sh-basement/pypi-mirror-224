"""Parse json config to swagger."""
import functools
import inspect
import json
from copy import deepcopy
from typing import Any, Callable, Optional, Set, Tuple, Union, cast

from rime_sdk.swagger.swagger_client.models import (
    DataInfoParamsFeatureIntersection,
    DataInfoParamsRankingInfo,
    ModelHuggingFaceModelInfo,
    ModelModelInfo,
    ModelModelPathInfo,
    RimeUUID,
    TestrunConnectionInfo,
    TestrunDataCollectorInfo,
    TestrunDataFileInfo,
    TestrunDataInfoParams,
    TestrunDataLoadingInfo,
    TestrunDeltaLakeInfo,
    TestrunHuggingFaceDataInfo,
    TestrunPredictionParams,
    TestrunPredInfo,
    TestrunSingleDataInfo,
)

DEFAULT_DO_SAMPLING = True
CONNECTION_INFO_TYPE_SWAGGER = Union[
    TestrunDataFileInfo,
    TestrunDataLoadingInfo,
    TestrunDataCollectorInfo,
    TestrunDeltaLakeInfo,
    TestrunHuggingFaceDataInfo,
]
VALID_CONNECTION_TYPES = [
    "data_file",
    "data_loading",
    "data_collector",
    "delta_lake",
    "hugging_face",
]


def validate_types(func: Callable) -> Callable:
    """Wrap given function with a decorator that validates types of arguments."""

    @functools.wraps(func)
    def wrapper_validate(*args: Any, **kwargs: Any) -> Any:
        # https://docs.python.org/3.7/library/inspect.html#inspect.getfullargspec
        argspec = inspect.getfullargspec(func)
        for arg, argname in zip(args, argspec.args):
            typ = argspec.annotations[argname]
            if hasattr(typ, "__origin__"):
                # convert generic types to their origin, e.g. List[dict] -> list
                # (so typ can be used with isinstance)
                typ = typ.__origin__
            if not isinstance(arg, typ):
                raise TypeError(
                    f"Expected argument of type {typ} for parameter '{argname}'. "
                    f"Got {type(arg)}."
                )
        return func(*args, **kwargs)

    return wrapper_validate


# NOTE: whenever changing any of convert_single_pred_info_to_swagger,
# convert_single_data_info_to_swagger, convert_model_info_to_swagger, or any of their
# helper functions, be sure to copy those changes over to rime/core/config_parser.py.
# This is needed for the mock registry used in rime-engine ete tests.
@validate_types
def convert_pred_params_to_swagger(
    pred_params: dict,
) -> Optional[TestrunPredictionParams]:
    """Convert prediction params dictionary to swagger."""
    _config = deepcopy(pred_params)
    proto_names = TestrunPredictionParams.swagger_types
    param_config = {
        name: _config.pop(name) for name in proto_names if name in pred_params
    }
    if len(param_config) == 0:
        return None
    if _config:
        raise ValueError(
            f"Unknown prediction params: {list(_config)}"
            f"\nExpected: {list(proto_names)}"
        )
    return TestrunPredictionParams(**param_config)


@validate_types
def convert_data_params_to_swagger(
    data_params: dict,
) -> Optional[TestrunDataInfoParams]:
    """Convert data params dictionary to swagger."""
    field_names = TestrunDataInfoParams.swagger_types
    _config = deepcopy(data_params)
    param_config = {
        name: _config.pop(name) for name in field_names if name in data_params
    }
    if "sample" not in param_config:
        param_config["sample"] = DEFAULT_DO_SAMPLING
    if len(param_config) == 0:
        return None
    if _config:
        raise ValueError(
            "Found parameters in the data_params config that do"
            f" not belong: {list(_config)}"
            f"\nExpected: {list(field_names)}"
        )
    if "loading_kwargs" in param_config and param_config["loading_kwargs"] is not None:
        param_config["loading_kwargs"] = json.dumps(param_config["loading_kwargs"])
    if "ranking_info" in param_config and param_config["ranking_info"] is not None:
        param_config["ranking_info"] = DataInfoParamsRankingInfo(
            **param_config["ranking_info"]
        )
    if "intersections" in param_config and param_config["intersections"] is not None:
        intersections = param_config["intersections"]
        param_config["intersections"] = [
            DataInfoParamsFeatureIntersection(features=i.get("features", []))
            for i in intersections
        ]
    for param in ["text_features", "image_features"]:
        unstructured_feats = param_config.get(param)
        if unstructured_feats is not None and not isinstance(unstructured_feats, list):
            raise ValueError(
                f"`{param}` must be type `List[str]`. Got '{unstructured_feats}'."
            )
    return TestrunDataInfoParams(**param_config)


@validate_types
def _mutate_data_file_conn_info_to_swag(
    connection_info: dict, path: str
) -> TestrunDataFileInfo:
    """Process data file connection info into a connection swagger."""
    required_keys = {"path"}
    _check_required_keys_exist(connection_info, required_keys, path)
    return TestrunDataFileInfo(path=connection_info.pop("path"))


@validate_types
def _mutate_data_loader_conn_info_to_swag(
    connection_info: dict, path: str
) -> TestrunDataLoadingInfo:
    """Process data loader connection info into a connection swagger."""
    required_keys = {"path", "load_func_name"}
    _check_required_keys_exist(connection_info, required_keys, path)
    loader_kwargs_json = ""
    if "loader_kwargs" in connection_info and "loader_kwargs_json" in connection_info:
        raise ValueError(
            "Got both loader_kwargs and loader_kwargs_json, "
            "but only one should be provided."
        )
    elif "loader_kwargs" in connection_info:
        # This can be None, but we don't want to set, so check first.
        _val = connection_info.pop("loader_kwargs")
        if _val is not None:
            loader_kwargs_json = json.dumps(_val)
    elif "loader_kwargs_json" in connection_info:
        # This can be None, but we don't want to set, so check first.
        _val = connection_info.pop("loader_kwargs_json")
        if _val is not None:
            loader_kwargs_json = _val
    else:
        pass
    return TestrunDataLoadingInfo(
        path=connection_info.pop("path"),
        load_func_name=connection_info.pop("load_func_name"),
        loader_kwargs_json=loader_kwargs_json,
    )


@validate_types
def _mutate_data_collector_conn_info_to_swag(
    connection_info: dict, path: str
) -> TestrunDataCollectorInfo:
    """Process data collector connection info into a connection info swagger."""
    required_keys = {"data_stream_id"}
    _check_required_keys_exist(connection_info, required_keys, path)
    data_stream_id = RimeUUID(connection_info.pop("data_stream_id"))
    return TestrunDataCollectorInfo(data_stream_id=data_stream_id)


@validate_types
def _mutate_delta_lake_conn_info_to_swag(
    connection_info: dict, path: str
) -> TestrunDeltaLakeInfo:
    """Process delta lake connection info into a connection info swagger."""
    required_keys = {"table_name"}
    _check_required_keys_exist(connection_info, required_keys, path)
    return TestrunDeltaLakeInfo(table_name=connection_info.pop("table_name"))


@validate_types
def _mutate_huggingface_conn_info_to_swag(
    connection_info: dict, path: str
) -> TestrunHuggingFaceDataInfo:
    """Process huggingface connection info into a connection info swagger."""
    required_keys = {"dataset_uri", "split_name"}
    _check_required_keys_exist(connection_info, required_keys, path)
    return TestrunHuggingFaceDataInfo(
        dataset_uri=connection_info.pop("dataset_uri"),
        split_name=connection_info.pop("split_name", None),
        loading_params_json=json.dumps(connection_info.pop("loading_params", None)),
    )


def _check_required_keys_exist(
    config: dict, required_keys: Set[str], path: str
) -> None:
    """Check that required keys exist in the configuration."""
    missing_keys = required_keys.difference(config)
    if missing_keys:
        raise ValueError(
            f"Missing arguments for {missing_keys} in {path}.\n"
            f"Expected: {list(required_keys)}\n"
            f"Got: {list(config.keys())}"
        )


def process_connection_info_to_swagger(
    connection_info: dict, config_type: str, path: str
) -> CONNECTION_INFO_TYPE_SWAGGER:
    """Process config connection info into a connection swagger and its swagger key."""
    _config = deepcopy(connection_info)
    _config = _config.pop(config_type)
    connection_loader_map = {
        "data_file": _mutate_data_file_conn_info_to_swag,
        "data_loading": _mutate_data_loader_conn_info_to_swag,
        "data_collector": _mutate_data_collector_conn_info_to_swag,
        "delta_lake": _mutate_delta_lake_conn_info_to_swag,
        "hugging_face": _mutate_huggingface_conn_info_to_swag,
    }
    _path = f"{path}.{config_type}"
    swagger = connection_loader_map[config_type](_config, _path)
    if _config:
        expected_field_names = getattr(swagger, "swagger_types", [])
        raise ValueError(
            f"Found parameters in the connection_info config of type {config_type}"
            f" that do not belong: {list(_config)}."
            f" Expected parameters: {expected_field_names}."
        )
    return cast(CONNECTION_INFO_TYPE_SWAGGER, swagger)


@validate_types
def convert_single_pred_info_to_swagger(pred_config: dict) -> Optional[TestrunPredInfo]:
    """Convert a dictionary to single pred info swagger message."""
    _config = deepcopy(pred_config)
    if "connection_info" not in _config:
        raise ValueError(
            "Missing required key 'connection_info' in prediction info config."
            f"\nGot: {list(_config)}."
        )
    connection_info = _config.pop("connection_info")
    pred_params_dict = _config.pop("pred_params", {})
    pred_params = convert_pred_params_to_swagger(pred_params_dict)
    connection_swagger, field = _process_connection_info_dict_swagger(
        connection_info, "pred_config"
    )
    connection_info = TestrunConnectionInfo()
    setattr(connection_info, field, connection_swagger)
    return TestrunPredInfo(pred_params=pred_params, connection_info=connection_info)


@validate_types
def _process_connection_info_dict_swagger(
    connection_info: dict, path: str
) -> Tuple[CONNECTION_INFO_TYPE_SWAGGER, str]:
    """Process the connection info dictionary."""
    if not connection_info:
        raise ValueError(f"No connection_info provided under {path}")
    config_type = list(connection_info.keys())[0]
    if len(connection_info) > 1:
        raise ValueError(
            f"Found parameters in the connection info config for {path} that do not"
            f" belong: {list(connection_info)}."
            f" Expected one of {VALID_CONNECTION_TYPES}."
        )
    if config_type not in VALID_CONNECTION_TYPES:
        raise ValueError(
            "Must specify connection type as part of `connection_info` in config. "
            f"Valid connection types are: {VALID_CONNECTION_TYPES}. Provided "
            f"connection_info of {path}.{connection_info}."
        )
    _path = f"{path}.connection_info"
    connection_swagger = process_connection_info_to_swagger(
        connection_info, config_type, _path
    )
    return connection_swagger, config_type


@validate_types
def convert_single_data_info_to_swagger(data_config: dict) -> TestrunSingleDataInfo:
    """Convert a dictionary to a `SingleDataInfo` Swagger message."""
    _config = deepcopy(data_config)
    if "connection_info" not in _config:
        raise ValueError(
            "Missing required key `connection_info` in data info config."
            f"\nGot: {list(_config)}"
        )
    connection_info = _config.pop("connection_info")
    path = "data_info"
    connection_swagger, field = _process_connection_info_dict_swagger(
        connection_info, path
    )
    params_dict = _config.pop("data_params", {})
    data_params = convert_data_params_to_swagger(params_dict)
    if _config:
        raise ValueError(
            f"Found parameters in the data info config for {path} that do not"
            f" belong: {list(_config)}."
            f" Expected parameters: {list(TestrunSingleDataInfo.swagger_types)}."
        )
    connection_info = TestrunConnectionInfo()
    setattr(connection_info, field, connection_swagger)
    return TestrunSingleDataInfo(
        data_params=data_params, connection_info=connection_info,
    )


@validate_types
def convert_model_info_to_swagger(model_config: dict) -> ModelModelInfo:
    """Convert a dictionary to model info swagger message."""
    _config = deepcopy(model_config)
    valid_model_infos = list(ModelModelInfo.swagger_types)
    if len(_config) != 1:
        raise ValueError(
            "Must specify exactly one valid model_info type in config. "
            f"Valid model_info types are: {valid_model_infos}. "
            f"Got: {list(_config)}."
        )
    model_type, model_info = next(iter(_config.items()))
    if not isinstance(model_info, dict):
        raise ValueError(
            f"model_info must be a dictionary. Got: {type(model_info)}."
            f"\nFull config: {model_config}"
        )
    try:
        if model_type == "model_path":
            model_info_swagger = ModelModelInfo(
                model_path=ModelModelPathInfo(path=model_info.pop("path"))
            )
        elif model_type == "hugging_face":
            model_uri = model_info.pop("model_uri")
            config_d = model_info.pop("kwargs", {})
            if isinstance(config_d, dict):
                config_str = json.dumps(config_d)
            elif isinstance(config_d, str):
                config_str = config_d
            else:
                raise ValueError(
                    f"Invalid type for `kwargs` in hugging_face model_info."
                    f" Expected `dict` or json `str`. Got: {type(config_d)}"
                )
            model_info_swagger = ModelModelInfo(
                hugging_face=ModelHuggingFaceModelInfo(
                    model_uri=model_uri, kwargs=config_str
                )
            )
        else:
            raise ValueError(
                f"model_info type in config should be one of {valid_model_infos}. "
                f"Got {model_type}."
            )
    except KeyError as e:
        raise ValueError(f"Invalid config: {model_config}") from e

    if model_info:
        oneof_object = getattr(model_info_swagger, model_type)
        expected_field_names = getattr(oneof_object, "swagger_types", [])
        raise ValueError(
            f"Found parameters in the model_info config of type {model_type}"
            f" that do not belong: {list(model_info)}."
            f" Expected parameters: {expected_field_names}."
        )
    return model_info_swagger


def _get_uuid(id_str: str) -> dict:
    return {"uuid": id_str}


def _get_individual_tests_config_swagger(individual_tests_config: dict) -> str:
    try:
        return json.dumps(individual_tests_config)
    except TypeError:
        raise ValueError("The provided individual_tests_config was not valid JSON.")
