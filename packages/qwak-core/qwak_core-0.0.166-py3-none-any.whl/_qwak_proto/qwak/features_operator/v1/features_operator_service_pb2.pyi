"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import qwak.features_operator.v1.features_operator_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BaseValidationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTO_DEFINITION_FIELD_NUMBER: builtins.int
    IMPORTS_FIELD_NUMBER: builtins.int
    NUMBER_OF_SAMPLES_FIELD_NUMBER: builtins.int
    proto_definition: builtins.str
    """Proto definition to execute on Livy"""
    imports: builtins.str
    """Imports needed for the proto definition"""
    number_of_samples: builtins.int
    """Number of samples to return from the data source"""
    def __init__(
        self,
        *,
        proto_definition: builtins.str = ...,
        imports: builtins.str = ...,
        number_of_samples: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["imports", b"imports", "number_of_samples", b"number_of_samples", "proto_definition", b"proto_definition"]) -> None: ...

global___BaseValidationRequest = BaseValidationRequest

class ValidateDataSourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_FIELD_NUMBER: builtins.int
    @property
    def request(self) -> global___BaseValidationRequest:
        """Base request properties"""
    def __init__(
        self,
        *,
        request: global___BaseValidationRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["request", b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["request", b"request"]) -> None: ...

global___ValidateDataSourceRequest = ValidateDataSourceRequest

class ValidateFeatureSetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_FIELD_NUMBER: builtins.int
    S3_UDF_ZIP_PATH_FIELD_NUMBER: builtins.int
    @property
    def request(self) -> global___BaseValidationRequest:
        """Base request properties"""
    s3_udf_zip_path: builtins.str
    """S3 UDF ZIP path"""
    def __init__(
        self,
        *,
        request: global___BaseValidationRequest | None = ...,
        s3_udf_zip_path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["request", b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["request", b"request", "s3_udf_zip_path", b"s3_udf_zip_path"]) -> None: ...

global___ValidateFeatureSetRequest = ValidateFeatureSetRequest

class ValidationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_RESPONSE_FIELD_NUMBER: builtins.int
    FAILURE_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def success_response(self) -> qwak.features_operator.v1.features_operator_pb2.ValidationSuccessResponse: ...
    @property
    def failure_response(self) -> qwak.features_operator.v1.features_operator_pb2.ValidationFailureResponse: ...
    def __init__(
        self,
        *,
        success_response: qwak.features_operator.v1.features_operator_pb2.ValidationSuccessResponse | None = ...,
        failure_response: qwak.features_operator.v1.features_operator_pb2.ValidationFailureResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["failure_response", b"failure_response", "success_response", b"success_response", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure_response", b"failure_response", "success_response", b"success_response", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["success_response", "failure_response"] | None: ...

global___ValidationResponse = ValidationResponse
