# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_file_subscription_response_body import CreateFileSubscriptionResponseBody


class CreateFileSubscriptionResponse(BaseResponse):
    _types = {
        "data": CreateFileSubscriptionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateFileSubscriptionResponseBody] = None
        init(self, d, self._types)
