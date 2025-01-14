# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_permission_member import MailgroupPermissionMember


class BatchCreateMailgroupPermissionMemberResponseBody(object):
    _types = {
        "items": List[MailgroupPermissionMember],
    }

    def __init__(self, d=None):
        self.items: Optional[List[MailgroupPermissionMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateMailgroupPermissionMemberResponseBodyBuilder":
        return BatchCreateMailgroupPermissionMemberResponseBodyBuilder()


class BatchCreateMailgroupPermissionMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_mailgroup_permission_member_response_body = BatchCreateMailgroupPermissionMemberResponseBody()

    def items(self,
              items: List[MailgroupPermissionMember]) -> "BatchCreateMailgroupPermissionMemberResponseBodyBuilder":
        self._batch_create_mailgroup_permission_member_response_body.items = items
        return self

    def build(self) -> "BatchCreateMailgroupPermissionMemberResponseBody":
        return self._batch_create_mailgroup_permission_member_response_body
