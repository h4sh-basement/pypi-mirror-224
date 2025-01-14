# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .auth_permission_member_response_body import AuthPermissionMemberResponseBody


class AuthPermissionMemberResponse(BaseResponse):
    _types = {
        "data": AuthPermissionMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[AuthPermissionMemberResponseBody] = None
        init(self, d, self._types)
