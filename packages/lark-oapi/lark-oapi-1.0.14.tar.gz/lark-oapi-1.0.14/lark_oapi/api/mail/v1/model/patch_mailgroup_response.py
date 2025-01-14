# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_mailgroup_response_body import PatchMailgroupResponseBody


class PatchMailgroupResponse(BaseResponse):
    _types = {
        "data": PatchMailgroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchMailgroupResponseBody] = None
        init(self, d, self._types)
