# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_schema_response_body import CreateSchemaResponseBody


class CreateSchemaResponse(BaseResponse):
    _types = {
        "data": CreateSchemaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateSchemaResponseBody] = None
        init(self, d, self._types)
