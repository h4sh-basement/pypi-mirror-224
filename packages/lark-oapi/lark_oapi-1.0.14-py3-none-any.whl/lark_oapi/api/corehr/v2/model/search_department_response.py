# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_department_response_body import SearchDepartmentResponseBody


class SearchDepartmentResponse(BaseResponse):
    _types = {
        "data": SearchDepartmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchDepartmentResponseBody] = None
        init(self, d, self._types)
