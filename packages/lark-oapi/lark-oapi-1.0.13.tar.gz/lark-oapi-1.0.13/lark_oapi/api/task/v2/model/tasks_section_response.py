# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .tasks_section_response_body import TasksSectionResponseBody


class TasksSectionResponse(BaseResponse):
    _types = {
        "data": TasksSectionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[TasksSectionResponseBody] = None
        init(self, d, self._types)
