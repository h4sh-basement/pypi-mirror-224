# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ProgressRate(object):
    _types = {
        "percent": int,
        "status": int,
    }

    def __init__(self, d=None):
        self.percent: Optional[int] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProgressRateBuilder":
        return ProgressRateBuilder()


class ProgressRateBuilder(object):
    def __init__(self) -> None:
        self._progress_rate = ProgressRate()

    def percent(self, percent: int) -> "ProgressRateBuilder":
        self._progress_rate.percent = percent
        return self

    def status(self, status: int) -> "ProgressRateBuilder":
        self._progress_rate.status = status
        return self

    def build(self) -> "ProgressRate":
        return self._progress_rate
