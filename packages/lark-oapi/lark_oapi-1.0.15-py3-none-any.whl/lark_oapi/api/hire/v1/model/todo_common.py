# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TodoCommon(object):
    _types = {
        "talent_id": str,
        "job_id": str,
        "application_id": str,
        "id": str,
    }

    def __init__(self, d=None):
        self.talent_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TodoCommonBuilder":
        return TodoCommonBuilder()


class TodoCommonBuilder(object):
    def __init__(self) -> None:
        self._todo_common = TodoCommon()

    def talent_id(self, talent_id: str) -> "TodoCommonBuilder":
        self._todo_common.talent_id = talent_id
        return self

    def job_id(self, job_id: str) -> "TodoCommonBuilder":
        self._todo_common.job_id = job_id
        return self

    def application_id(self, application_id: str) -> "TodoCommonBuilder":
        self._todo_common.application_id = application_id
        return self

    def id(self, id: str) -> "TodoCommonBuilder":
        self._todo_common.id = id
        return self

    def build(self) -> "TodoCommon":
        return self._todo_common
