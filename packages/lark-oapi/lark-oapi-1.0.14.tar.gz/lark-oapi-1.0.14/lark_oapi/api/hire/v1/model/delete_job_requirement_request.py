# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteJobRequirementRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_requirement_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteJobRequirementRequestBuilder":
        return DeleteJobRequirementRequestBuilder()


class DeleteJobRequirementRequestBuilder(object):

    def __init__(self) -> None:
        delete_job_requirement_request = DeleteJobRequirementRequest()
        delete_job_requirement_request.http_method = HttpMethod.DELETE
        delete_job_requirement_request.uri = "/open-apis/hire/v1/job_requirements/:job_requirement_id"
        delete_job_requirement_request.token_types = {AccessTokenType.TENANT}
        self._delete_job_requirement_request: DeleteJobRequirementRequest = delete_job_requirement_request

    def job_requirement_id(self, job_requirement_id: str) -> "DeleteJobRequirementRequestBuilder":
        self._delete_job_requirement_request.job_requirement_id = job_requirement_id
        self._delete_job_requirement_request.paths["job_requirement_id"] = str(job_requirement_id)
        return self

    def build(self) -> DeleteJobRequirementRequest:
        return self._delete_job_requirement_request
