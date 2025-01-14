# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .base_member import BaseMember


class UpdatePermissionMemberResponseBody(object):
    _types = {
        "member": BaseMember,
    }

    def __init__(self, d=None):
        self.member: Optional[BaseMember] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdatePermissionMemberResponseBodyBuilder":
        return UpdatePermissionMemberResponseBodyBuilder()


class UpdatePermissionMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_permission_member_response_body = UpdatePermissionMemberResponseBody()

    def member(self, member: BaseMember) -> "UpdatePermissionMemberResponseBodyBuilder":
        self._update_permission_member_response_body.member = member
        return self

    def build(self) -> "UpdatePermissionMemberResponseBody":
        return self._update_permission_member_response_body
