# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RecordingPermissionObject(object):
    _types = {
        "id": str,
        "type": int,
        "permission": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.type: Optional[int] = None
        self.permission: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecordingPermissionObjectBuilder":
        return RecordingPermissionObjectBuilder()


class RecordingPermissionObjectBuilder(object):
    def __init__(self) -> None:
        self._recording_permission_object = RecordingPermissionObject()

    def id(self, id: str) -> "RecordingPermissionObjectBuilder":
        self._recording_permission_object.id = id
        return self

    def type(self, type: int) -> "RecordingPermissionObjectBuilder":
        self._recording_permission_object.type = type
        return self

    def permission(self, permission: int) -> "RecordingPermissionObjectBuilder":
        self._recording_permission_object.permission = permission
        return self

    def build(self) -> "RecordingPermissionObject":
        return self._recording_permission_object
