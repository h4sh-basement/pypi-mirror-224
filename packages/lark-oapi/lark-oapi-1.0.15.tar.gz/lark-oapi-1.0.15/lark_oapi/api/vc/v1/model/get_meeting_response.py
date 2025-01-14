# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_meeting_response_body import GetMeetingResponseBody


class GetMeetingResponse(BaseResponse):
    _types = {
        "data": GetMeetingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetMeetingResponseBody] = None
        init(self, d, self._types)
