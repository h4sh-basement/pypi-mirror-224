# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .system_status_user_close_result_entity import SystemStatusUserCloseResultEntity


class BatchCloseSystemStatusResponseBody(object):
    _types = {
        "result_list": List[SystemStatusUserCloseResultEntity],
    }

    def __init__(self, d=None):
        self.result_list: Optional[List[SystemStatusUserCloseResultEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCloseSystemStatusResponseBodyBuilder":
        return BatchCloseSystemStatusResponseBodyBuilder()


class BatchCloseSystemStatusResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_close_system_status_response_body = BatchCloseSystemStatusResponseBody()

    def result_list(self, result_list: List[
        SystemStatusUserCloseResultEntity]) -> "BatchCloseSystemStatusResponseBodyBuilder":
        self._batch_close_system_status_response_body.result_list = result_list
        return self

    def build(self) -> "BatchCloseSystemStatusResponseBody":
        return self._batch_close_system_status_response_body
