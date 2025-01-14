# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Hrbp(object):
    _types = {
        "employment_id_list": List[str],
        "department_id": str,
        "work_location_id": str,
    }

    def __init__(self, d=None):
        self.employment_id_list: Optional[List[str]] = None
        self.department_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "HrbpBuilder":
        return HrbpBuilder()


class HrbpBuilder(object):
    def __init__(self) -> None:
        self._hrbp = Hrbp()

    def employment_id_list(self, employment_id_list: List[str]) -> "HrbpBuilder":
        self._hrbp.employment_id_list = employment_id_list
        return self

    def department_id(self, department_id: str) -> "HrbpBuilder":
        self._hrbp.department_id = department_id
        return self

    def work_location_id(self, work_location_id: str) -> "HrbpBuilder":
        self._hrbp.work_location_id = work_location_id
        return self

    def build(self) -> "Hrbp":
        return self._hrbp
