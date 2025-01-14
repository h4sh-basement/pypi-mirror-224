# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_workplace_block_access_data_response_body import SearchWorkplaceBlockAccessDataResponseBody


class SearchWorkplaceBlockAccessDataResponse(BaseResponse):
    _types = {
        "data": SearchWorkplaceBlockAccessDataResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchWorkplaceBlockAccessDataResponseBody] = None
        init(self, d, self._types)
