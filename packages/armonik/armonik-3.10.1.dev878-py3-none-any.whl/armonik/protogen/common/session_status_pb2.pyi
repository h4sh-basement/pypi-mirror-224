from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SESSION_STATUS_UNSPECIFIED: _ClassVar[SessionStatus]
    SESSION_STATUS_RUNNING: _ClassVar[SessionStatus]
    SESSION_STATUS_CANCELLED: _ClassVar[SessionStatus]
SESSION_STATUS_UNSPECIFIED: SessionStatus
SESSION_STATUS_RUNNING: SessionStatus
SESSION_STATUS_CANCELLED: SessionStatus
