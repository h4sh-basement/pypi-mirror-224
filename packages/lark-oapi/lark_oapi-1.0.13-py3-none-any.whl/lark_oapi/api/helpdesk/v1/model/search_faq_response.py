# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_faq_response_body import SearchFaqResponseBody


class SearchFaqResponse(BaseResponse):
    _types = {
        "data": SearchFaqResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchFaqResponseBody] = None
        init(self, d, self._types)
