# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_comment_response_body import GetCommentResponseBody


class GetCommentResponse(BaseResponse):
    _types = {
        "data": GetCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetCommentResponseBody] = None
        init(self, d, self._types)
