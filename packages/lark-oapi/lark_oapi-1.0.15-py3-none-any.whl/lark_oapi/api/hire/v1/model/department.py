# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Department(object):
    _types = {
        "id": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentBuilder":
        return DepartmentBuilder()


class DepartmentBuilder(object):
    def __init__(self) -> None:
        self._department = Department()

    def id(self, id: str) -> "DepartmentBuilder":
        self._department.id = id
        return self

    def name(self, name: str) -> "DepartmentBuilder":
        self._department.name = name
        return self

    def en_name(self, en_name: str) -> "DepartmentBuilder":
        self._department.en_name = en_name
        return self

    def build(self) -> "Department":
        return self._department
