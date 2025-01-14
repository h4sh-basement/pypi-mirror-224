# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteJobRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteJobRequestBuilder":
        return DeleteJobRequestBuilder()


class DeleteJobRequestBuilder(object):

    def __init__(self) -> None:
        delete_job_request = DeleteJobRequest()
        delete_job_request.http_method = HttpMethod.DELETE
        delete_job_request.uri = "/open-apis/corehr/v1/jobs/:job_id"
        delete_job_request.token_types = {AccessTokenType.TENANT}
        self._delete_job_request: DeleteJobRequest = delete_job_request

    def job_id(self, job_id: str) -> "DeleteJobRequestBuilder":
        self._delete_job_request.job_id = job_id
        self._delete_job_request.paths["job_id"] = str(job_id)
        return self

    def build(self) -> DeleteJobRequest:
        return self._delete_job_request
