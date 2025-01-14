# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_chat_moderation_response_body import GetChatModerationResponseBody


class GetChatModerationResponse(BaseResponse):
    _types = {
        "data": GetChatModerationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetChatModerationResponseBody] = None
        init(self, d, self._types)
