# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_mailgroup_member_response_body import ListMailgroupMemberResponseBody


class ListMailgroupMemberResponse(BaseResponse):
    _types = {
        "data": ListMailgroupMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListMailgroupMemberResponseBody] = None
        init(self, d, self._types)
