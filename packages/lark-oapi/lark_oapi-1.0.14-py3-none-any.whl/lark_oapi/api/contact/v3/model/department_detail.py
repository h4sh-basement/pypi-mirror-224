# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department_path import DepartmentPath
from .department_path_name import DepartmentPathName


class DepartmentDetail(object):
    _types = {
        "department_id": int,
        "department_name": DepartmentPathName,
        "department_path": DepartmentPath,
    }

    def __init__(self, d=None):
        self.department_id: Optional[int] = None
        self.department_name: Optional[DepartmentPathName] = None
        self.department_path: Optional[DepartmentPath] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentDetailBuilder":
        return DepartmentDetailBuilder()


class DepartmentDetailBuilder(object):
    def __init__(self) -> None:
        self._department_detail = DepartmentDetail()

    def department_id(self, department_id: int) -> "DepartmentDetailBuilder":
        self._department_detail.department_id = department_id
        return self

    def department_name(self, department_name: DepartmentPathName) -> "DepartmentDetailBuilder":
        self._department_detail.department_name = department_name
        return self

    def department_path(self, department_path: DepartmentPath) -> "DepartmentDetailBuilder":
        self._department_detail.department_path = department_path
        return self

    def build(self) -> "DepartmentDetail":
        return self._department_detail
