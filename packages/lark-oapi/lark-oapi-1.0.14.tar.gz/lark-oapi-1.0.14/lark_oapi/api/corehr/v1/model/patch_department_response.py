# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_department_response_body import PatchDepartmentResponseBody


class PatchDepartmentResponse(BaseResponse):
    _types = {
        "data": PatchDepartmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchDepartmentResponseBody] = None
        init(self, d, self._types)
