# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_employee_type_response_body import GetEmployeeTypeResponseBody


class GetEmployeeTypeResponse(BaseResponse):
    _types = {
        "data": GetEmployeeTypeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetEmployeeTypeResponseBody] = None
        init(self, d, self._types)
