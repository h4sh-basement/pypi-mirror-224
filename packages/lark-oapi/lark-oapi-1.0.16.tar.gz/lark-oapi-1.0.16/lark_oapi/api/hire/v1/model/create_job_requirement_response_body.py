# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_requirement_dto import JobRequirementDto


class CreateJobRequirementResponseBody(object):
    _types = {
        "job_requirement": JobRequirementDto,
    }

    def __init__(self, d=None):
        self.job_requirement: Optional[JobRequirementDto] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateJobRequirementResponseBodyBuilder":
        return CreateJobRequirementResponseBodyBuilder()


class CreateJobRequirementResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_job_requirement_response_body = CreateJobRequirementResponseBody()

    def job_requirement(self, job_requirement: JobRequirementDto) -> "CreateJobRequirementResponseBodyBuilder":
        self._create_job_requirement_response_body.job_requirement = job_requirement
        return self

    def build(self) -> "CreateJobRequirementResponseBody":
        return self._create_job_requirement_response_body
