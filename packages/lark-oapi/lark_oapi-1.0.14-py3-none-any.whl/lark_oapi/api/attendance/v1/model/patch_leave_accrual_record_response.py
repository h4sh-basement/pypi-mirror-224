# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_leave_accrual_record_response_body import PatchLeaveAccrualRecordResponseBody


class PatchLeaveAccrualRecordResponse(BaseResponse):
    _types = {
        "data": PatchLeaveAccrualRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchLeaveAccrualRecordResponseBody] = None
        init(self, d, self._types)
