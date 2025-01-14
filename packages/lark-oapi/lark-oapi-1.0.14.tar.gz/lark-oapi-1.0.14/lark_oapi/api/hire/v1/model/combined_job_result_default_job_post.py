# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CombinedJobResultDefaultJobPost(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedJobResultDefaultJobPostBuilder":
        return CombinedJobResultDefaultJobPostBuilder()


class CombinedJobResultDefaultJobPostBuilder(object):
    def __init__(self) -> None:
        self._combined_job_result_default_job_post = CombinedJobResultDefaultJobPost()

    def id(self, id: str) -> "CombinedJobResultDefaultJobPostBuilder":
        self._combined_job_result_default_job_post.id = id
        return self

    def build(self) -> "CombinedJobResultDefaultJobPost":
        return self._combined_job_result_default_job_post
