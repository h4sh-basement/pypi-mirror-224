# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTaskRequestBuilder":
        return DeleteTaskRequestBuilder()


class DeleteTaskRequestBuilder(object):

    def __init__(self) -> None:
        delete_task_request = DeleteTaskRequest()
        delete_task_request.http_method = HttpMethod.DELETE
        delete_task_request.uri = "/open-apis/task/v1/tasks/:task_id"
        delete_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_task_request: DeleteTaskRequest = delete_task_request

    def task_id(self, task_id: str) -> "DeleteTaskRequestBuilder":
        self._delete_task_request.task_id = task_id
        self._delete_task_request.paths["task_id"] = str(task_id)
        return self

    def build(self) -> DeleteTaskRequest:
        return self._delete_task_request
