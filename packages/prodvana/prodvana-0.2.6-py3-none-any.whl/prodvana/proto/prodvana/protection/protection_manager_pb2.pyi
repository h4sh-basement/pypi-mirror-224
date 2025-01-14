"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import prodvana.proto.prodvana.protection.object_pb2
import prodvana.proto.prodvana.protection.protection_config_pb2
import prodvana.proto.prodvana.version.source_metadata_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ConfigureProtectionReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTION_CONFIG_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    SOURCE_METADATA_FIELD_NUMBER: builtins.int
    @property
    def protection_config(self) -> prodvana.proto.prodvana.protection.protection_config_pb2.ProtectionConfig: ...
    source: prodvana.proto.prodvana.version.source_metadata_pb2.Source.ValueType
    @property
    def source_metadata(self) -> prodvana.proto.prodvana.version.source_metadata_pb2.SourceMetadata: ...
    def __init__(
        self,
        *,
        protection_config: prodvana.proto.prodvana.protection.protection_config_pb2.ProtectionConfig | None = ...,
        source: prodvana.proto.prodvana.version.source_metadata_pb2.Source.ValueType = ...,
        source_metadata: prodvana.proto.prodvana.version.source_metadata_pb2.SourceMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["protection_config", b"protection_config", "source_metadata", b"source_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["protection_config", b"protection_config", "source", b"source", "source_metadata", b"source_metadata"]) -> None: ...

global___ConfigureProtectionReq = ConfigureProtectionReq

class ConfigureProtectionResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTION_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    protection_id: builtins.str
    version: builtins.str
    def __init__(
        self,
        *,
        protection_id: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["protection_id", b"protection_id", "version", b"version"]) -> None: ...

global___ConfigureProtectionResp = ConfigureProtectionResp

class ValidateConfigureProtectionResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ValidateConfigureProtectionResp = ValidateConfigureProtectionResp

class ListProtectionsReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    page_size: builtins.int
    def __init__(
        self,
        *,
        page_token: builtins.str = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListProtectionsReq = ListProtectionsReq

class ListProtectionsResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def protections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[prodvana.proto.prodvana.protection.object_pb2.Protection]: ...
    next_page_token: builtins.str
    def __init__(
        self,
        *,
        protections: collections.abc.Iterable[prodvana.proto.prodvana.protection.object_pb2.Protection] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "protections", b"protections"]) -> None: ...

global___ListProtectionsResp = ListProtectionsResp

class GetProtectionReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTION_FIELD_NUMBER: builtins.int
    protection: builtins.str
    def __init__(
        self,
        *,
        protection: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["protection", b"protection"]) -> None: ...

global___GetProtectionReq = GetProtectionReq

class GetProtectionResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTION_FIELD_NUMBER: builtins.int
    @property
    def protection(self) -> prodvana.proto.prodvana.protection.object_pb2.Protection: ...
    def __init__(
        self,
        *,
        protection: prodvana.proto.prodvana.protection.object_pb2.Protection | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["protection", b"protection"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["protection", b"protection"]) -> None: ...

global___GetProtectionResp = GetProtectionResp

class GetProtectionConfigReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTECTION_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    protection: builtins.str
    version: builtins.str
    """omit to get latest version"""
    def __init__(
        self,
        *,
        protection: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["protection", b"protection", "version", b"version"]) -> None: ...

global___GetProtectionConfigReq = GetProtectionConfigReq

class GetProtectionConfigResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> prodvana.proto.prodvana.protection.protection_config_pb2.ProtectionConfig: ...
    version: builtins.str
    def __init__(
        self,
        *,
        config: prodvana.proto.prodvana.protection.protection_config_pb2.ProtectionConfig | None = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "version", b"version"]) -> None: ...

global___GetProtectionConfigResp = GetProtectionConfigResp

class GetProtectionAttachmentConfigReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTACHMENT_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    attachment_id: builtins.str
    version: builtins.str
    """omit to get latest version"""
    def __init__(
        self,
        *,
        attachment_id: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attachment_id", b"attachment_id", "version", b"version"]) -> None: ...

global___GetProtectionAttachmentConfigReq = GetProtectionAttachmentConfigReq

class GetProtectionAttachmentConfigResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> prodvana.proto.prodvana.protection.protection_config_pb2.CompiledProtectionAttachmentConfig: ...
    version: builtins.str
    def __init__(
        self,
        *,
        config: prodvana.proto.prodvana.protection.protection_config_pb2.CompiledProtectionAttachmentConfig | None = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "version", b"version"]) -> None: ...

global___GetProtectionAttachmentConfigResp = GetProtectionAttachmentConfigResp
