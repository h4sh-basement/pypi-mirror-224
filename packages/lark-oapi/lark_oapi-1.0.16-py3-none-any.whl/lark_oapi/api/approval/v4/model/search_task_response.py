# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_task_response_body import SearchTaskResponseBody


class SearchTaskResponse(BaseResponse):
    _types = {
        "data": SearchTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchTaskResponseBody] = None
        init(self, d, self._types)
