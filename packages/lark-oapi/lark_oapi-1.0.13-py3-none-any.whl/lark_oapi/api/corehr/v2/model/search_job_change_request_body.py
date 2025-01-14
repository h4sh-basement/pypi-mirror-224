# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SearchJobChangeRequestBody(object):
    _types = {
        "employment_ids": List[str],
        "job_change_ids": List[str],
        "statuses": List[str],
    }

    def __init__(self, d=None):
        self.employment_ids: Optional[List[str]] = None
        self.job_change_ids: Optional[List[str]] = None
        self.statuses: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchJobChangeRequestBodyBuilder":
        return SearchJobChangeRequestBodyBuilder()


class SearchJobChangeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_job_change_request_body = SearchJobChangeRequestBody()

    def employment_ids(self, employment_ids: List[str]) -> "SearchJobChangeRequestBodyBuilder":
        self._search_job_change_request_body.employment_ids = employment_ids
        return self

    def job_change_ids(self, job_change_ids: List[str]) -> "SearchJobChangeRequestBodyBuilder":
        self._search_job_change_request_body.job_change_ids = job_change_ids
        return self

    def statuses(self, statuses: List[str]) -> "SearchJobChangeRequestBodyBuilder":
        self._search_job_change_request_body.statuses = statuses
        return self

    def build(self) -> "SearchJobChangeRequestBody":
        return self._search_job_change_request_body
