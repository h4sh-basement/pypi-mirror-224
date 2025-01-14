# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_offboarding_response_body import SearchOffboardingResponseBody


class SearchOffboardingResponse(BaseResponse):
    _types = {
        "data": SearchOffboardingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchOffboardingResponseBody] = None
        init(self, d, self._types)
