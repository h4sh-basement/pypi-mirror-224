# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_exchange_binding_response_body import CreateExchangeBindingResponseBody


class CreateExchangeBindingResponse(BaseResponse):
    _types = {
        "data": CreateExchangeBindingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateExchangeBindingResponseBody] = None
        init(self, d, self._types)
