# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ExternalGrantRoleInfo(object):
    _types = {
        "role_id": str,
    }

    def __init__(self, d=None):
        self.role_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalGrantRoleInfoBuilder":
        return ExternalGrantRoleInfoBuilder()


class ExternalGrantRoleInfoBuilder(object):
    def __init__(self) -> None:
        self._external_grant_role_info = ExternalGrantRoleInfo()

    def role_id(self, role_id: str) -> "ExternalGrantRoleInfoBuilder":
        self._external_grant_role_info.role_id = role_id
        return self

    def build(self) -> "ExternalGrantRoleInfo":
        return self._external_grant_role_info
