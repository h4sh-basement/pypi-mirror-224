"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import qwak.administration.account.v1.preferences_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AccountActivityStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AccountActivityStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccountActivityStatus.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_STATUS_INVALID: _AccountActivityStatus.ValueType  # 0
    """Default invalid State"""
    ACCOUNT_STATUS_ACTIVE: _AccountActivityStatus.ValueType  # 1
    """Marks the account is currently active in Qwak"""
    ACCOUNT_STATUS_DISABLED: _AccountActivityStatus.ValueType  # 2
    """Marks that the account is disabled"""

class AccountActivityStatus(_AccountActivityStatus, metaclass=_AccountActivityStatusEnumTypeWrapper): ...

ACCOUNT_STATUS_INVALID: AccountActivityStatus.ValueType  # 0
"""Default invalid State"""
ACCOUNT_STATUS_ACTIVE: AccountActivityStatus.ValueType  # 1
"""Marks the account is currently active in Qwak"""
ACCOUNT_STATUS_DISABLED: AccountActivityStatus.ValueType  # 2
"""Marks that the account is disabled"""
global___AccountActivityStatus = AccountActivityStatus

class _AccountType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AccountTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccountType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_TYPE_INVALID: _AccountType.ValueType  # 0
    """Default invalid account type"""
    HYBRID: _AccountType.ValueType  # 1
    """Hybrid account type"""
    SAAS: _AccountType.ValueType  # 2
    """Saas account type"""

class AccountType(_AccountType, metaclass=_AccountTypeEnumTypeWrapper): ...

ACCOUNT_TYPE_INVALID: AccountType.ValueType  # 0
"""Default invalid account type"""
HYBRID: AccountType.ValueType  # 1
"""Hybrid account type"""
SAAS: AccountType.ValueType  # 2
"""Saas account type"""
global___AccountType = AccountType

class Account(google.protobuf.message.Message):
    """An account represent a billable entity.
    users can be bind to account
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PREFERENCES_FIELD_NUMBER: builtins.int
    DEFAULT_ENVIRONMENT_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Assigned account ID"""
    name: builtins.str
    """Given account name"""
    status: global___AccountActivityStatus.ValueType
    """Current account status"""
    @property
    def preferences(self) -> qwak.administration.account.v1.preferences_pb2.AccountPreferences:
        """Account preferences"""
    default_environment_id: builtins.str
    """Account default environment"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation date"""
    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last modification date"""
    type: global___AccountType.ValueType
    """The type of the account"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        status: global___AccountActivityStatus.ValueType = ...,
        preferences: qwak.administration.account.v1.preferences_pb2.AccountPreferences | None = ...,
        default_environment_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        type: global___AccountType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "last_modified_at", b"last_modified_at", "preferences", b"preferences"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "default_environment_id", b"default_environment_id", "id", b"id", "last_modified_at", b"last_modified_at", "name", b"name", "preferences", b"preferences", "status", b"status", "type", b"type"]) -> None: ...

global___Account = Account

class ListAccountFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVITY_STATUS_FIELD_NUMBER: builtins.int
    activity_status: global___AccountActivityStatus.ValueType
    """Filter based on account activity status"""
    def __init__(
        self,
        *,
        activity_status: global___AccountActivityStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_status", b"activity_status"]) -> None: ...

global___ListAccountFilter = ListAccountFilter

class AutoBindingAccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    RULE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Id"""
    @property
    def rule(self) -> global___AutoBindingRule:
        """hostname to auto-bind"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        rule: global___AutoBindingRule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rule", b"rule"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "rule", b"rule"]) -> None: ...

global___AutoBindingAccount = AutoBindingAccount

class AutoBindingRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EMAIL_HOSTNAME_FIELD_NUMBER: builtins.int
    email_hostname: builtins.str
    """email_hostname to auto-bind"""
    def __init__(
        self,
        *,
        email_hostname: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["email_hostname", b"email_hostname"]) -> None: ...

global___AutoBindingRule = AutoBindingRule
