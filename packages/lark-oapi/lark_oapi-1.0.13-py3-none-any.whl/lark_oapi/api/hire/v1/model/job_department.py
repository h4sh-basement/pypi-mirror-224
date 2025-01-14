# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobDepartment(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDepartmentBuilder":
        return JobDepartmentBuilder()


class JobDepartmentBuilder(object):
    def __init__(self) -> None:
        self._job_department = JobDepartment()

    def id(self, id: str) -> "JobDepartmentBuilder":
        self._job_department.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobDepartmentBuilder":
        self._job_department.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobDepartmentBuilder":
        self._job_department.en_name = en_name
        return self

    def build(self) -> "JobDepartment":
        return self._job_department
