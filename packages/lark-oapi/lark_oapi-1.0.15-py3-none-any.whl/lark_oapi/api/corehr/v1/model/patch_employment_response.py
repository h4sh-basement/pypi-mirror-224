# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_employment_response_body import PatchEmploymentResponseBody


class PatchEmploymentResponse(BaseResponse):
    _types = {
        "data": PatchEmploymentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchEmploymentResponseBody] = None
        init(self, d, self._types)
