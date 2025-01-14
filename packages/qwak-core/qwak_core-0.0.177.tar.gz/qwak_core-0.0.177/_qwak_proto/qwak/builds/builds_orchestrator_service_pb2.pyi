"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import qwak.builds.build_pb2
import qwak.builds.build_url_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BuildModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_SPEC_FIELD_NUMBER: builtins.int
    @property
    def build_spec(self) -> qwak.builds.build_pb2.RemoteBuildSpec:
        """Requested build model spec"""
    def __init__(
        self,
        *,
        build_spec: qwak.builds.build_pb2.RemoteBuildSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["build_spec", b"build_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_spec", b"build_spec"]) -> None: ...

global___BuildModelRequest = BuildModelRequest

class BuildModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___BuildModelResponse = BuildModelResponse

class CancelBuildModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """Build id of the build to cancel"""
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_id", b"build_id"]) -> None: ...

global___CancelBuildModelRequest = CancelBuildModelRequest

class CancelBuildModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CancelBuildModelResponse = CancelBuildModelResponse

class CreateUploadURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """Model id"""
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_id", b"build_id"]) -> None: ...

global___CreateUploadURLRequest = CreateUploadURLRequest

class CreateUploadURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPLOAD_URL_FIELD_NUMBER: builtins.int
    DOWNLOAD_URL_FIELD_NUMBER: builtins.int
    upload_url: builtins.str
    """Upload url intended for the model code upload"""
    download_url: builtins.str
    """URL which will contain the content uploaded to the upload url"""
    def __init__(
        self,
        *,
        upload_url: builtins.str = ...,
        download_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["download_url", b"download_url", "upload_url", b"upload_url"]) -> None: ...

global___CreateUploadURLResponse = CreateUploadURLResponse

class GetBuildVersioningUploadURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> qwak.builds.build_url_pb2.BuildVersioningUrlParams:
        """The params to define the url."""
    def __init__(
        self,
        *,
        params: qwak.builds.build_url_pb2.BuildVersioningUrlParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___GetBuildVersioningUploadURLRequest = GetBuildVersioningUploadURLRequest

class GetBuildVersioningUploadURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPLOAD_URL_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    upload_url: builtins.str
    """Upload url intended for the upload"""
    path: builtins.str
    """The Path we saved the artifact in"""
    def __init__(
        self,
        *,
        upload_url: builtins.str = ...,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "upload_url", b"upload_url"]) -> None: ...

global___GetBuildVersioningUploadURLResponse = GetBuildVersioningUploadURLResponse

class GetBuildVersioningDownloadURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> qwak.builds.build_url_pb2.BuildVersioningUrlParams:
        """The params to define the url."""
    def __init__(
        self,
        *,
        params: qwak.builds.build_url_pb2.BuildVersioningUrlParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___GetBuildVersioningDownloadURLRequest = GetBuildVersioningDownloadURLRequest

class GetBuildVersioningDownloadURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOWNLOAD_URL_FIELD_NUMBER: builtins.int
    FILE_SIZE_FIELD_NUMBER: builtins.int
    download_url: builtins.str
    """Download url - to download the wanted artifact."""
    file_size: builtins.int
    """The size of the file."""
    def __init__(
        self,
        *,
        download_url: builtins.str = ...,
        file_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["download_url", b"download_url", "file_size", b"file_size"]) -> None: ...

global___GetBuildVersioningDownloadURLResponse = GetBuildVersioningDownloadURLResponse

class ListBuildVersioningTagsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_VERSIONING_TAGS_FIELD_NUMBER: builtins.int
    @property
    def build_versioning_tags(self) -> qwak.builds.build_url_pb2.BuildVersioningTags:
        """The params to define the urls."""
    def __init__(
        self,
        *,
        build_versioning_tags: qwak.builds.build_url_pb2.BuildVersioningTags | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["build_versioning_tags", b"build_versioning_tags"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_versioning_tags", b"build_versioning_tags"]) -> None: ...

global___ListBuildVersioningTagsRequest = ListBuildVersioningTagsRequest

class ListBuildVersioningTagsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_VERSIONING_TAGS_PROPERTIES_FIELD_NUMBER: builtins.int
    @property
    def build_versioning_tags_properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qwak.builds.build_url_pb2.BuildVersioningTagsProperties]:
        """Download urls - to download the wanted artifacts."""
    def __init__(
        self,
        *,
        build_versioning_tags_properties: collections.abc.Iterable[qwak.builds.build_url_pb2.BuildVersioningTagsProperties] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_versioning_tags_properties", b"build_versioning_tags_properties"]) -> None: ...

global___ListBuildVersioningTagsResponse = ListBuildVersioningTagsResponse

class CreateDataTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_ID_FIELD_NUMBER: builtins.int
    BUILD_ID_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    model_id: builtins.str
    """The model Id"""
    build_id: builtins.str
    """The build Id"""
    tag: builtins.str
    """The tag save data by."""
    @property
    def table(self) -> qwak.builds.build_pb2.DataTableDefinition:
        """Table Definition"""
    path: builtins.str
    """The path where the data is saved in"""
    def __init__(
        self,
        *,
        model_id: builtins.str = ...,
        build_id: builtins.str = ...,
        tag: builtins.str = ...,
        table: qwak.builds.build_pb2.DataTableDefinition | None = ...,
        path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["table", b"table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["build_id", b"build_id", "model_id", b"model_id", "path", b"path", "table", b"table", "tag", b"tag"]) -> None: ...

global___CreateDataTableRequest = CreateDataTableRequest

class CreateDataTableResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CreateDataTableResponse = CreateDataTableResponse

class GetBaseDockerImageNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_DOCKER_IMAGE_TYPE_FIELD_NUMBER: builtins.int
    base_docker_image_type: qwak.builds.build_pb2.BaseDockerImageType.ValueType
    def __init__(
        self,
        *,
        base_docker_image_type: qwak.builds.build_pb2.BaseDockerImageType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_docker_image_type", b"base_docker_image_type"]) -> None: ...

global___GetBaseDockerImageNameRequest = GetBaseDockerImageNameRequest

class GetBaseDockerImageNameResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_DOCKER_IMAGE_NAME_FIELD_NUMBER: builtins.int
    base_docker_image_name: builtins.str
    def __init__(
        self,
        *,
        base_docker_image_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_docker_image_name", b"base_docker_image_name"]) -> None: ...

global___GetBaseDockerImageNameResponse = GetBaseDockerImageNameResponse
