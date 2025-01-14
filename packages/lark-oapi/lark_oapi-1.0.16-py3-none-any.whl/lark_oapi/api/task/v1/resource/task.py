# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_delete_collaborator_task_request import BatchDeleteCollaboratorTaskRequest
from ..model.batch_delete_collaborator_task_response import BatchDeleteCollaboratorTaskResponse
from ..model.batch_delete_follower_task_request import BatchDeleteFollowerTaskRequest
from ..model.batch_delete_follower_task_response import BatchDeleteFollowerTaskResponse
from ..model.complete_task_request import CompleteTaskRequest
from ..model.complete_task_response import CompleteTaskResponse
from ..model.create_task_request import CreateTaskRequest
from ..model.create_task_response import CreateTaskResponse
from ..model.delete_task_request import DeleteTaskRequest
from ..model.delete_task_response import DeleteTaskResponse
from ..model.get_task_request import GetTaskRequest
from ..model.get_task_response import GetTaskResponse
from ..model.list_task_request import ListTaskRequest
from ..model.list_task_response import ListTaskResponse
from ..model.patch_task_request import PatchTaskRequest
from ..model.patch_task_response import PatchTaskResponse
from ..model.uncomplete_task_request import UncompleteTaskRequest
from ..model.uncomplete_task_response import UncompleteTaskResponse


class Task(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_delete_collaborator(self, request: BatchDeleteCollaboratorTaskRequest,
                                  option: Optional[RequestOption] = None) -> BatchDeleteCollaboratorTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteCollaboratorTaskResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                       BatchDeleteCollaboratorTaskResponse)
        response.raw = resp

        return response

    def batch_delete_follower(self, request: BatchDeleteFollowerTaskRequest,
                              option: Optional[RequestOption] = None) -> BatchDeleteFollowerTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteFollowerTaskResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   BatchDeleteFollowerTaskResponse)
        response.raw = resp

        return response

    def complete(self, request: CompleteTaskRequest, option: Optional[RequestOption] = None) -> CompleteTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CompleteTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), CompleteTaskResponse)
        response.raw = resp

        return response

    def create(self, request: CreateTaskRequest, option: Optional[RequestOption] = None) -> CreateTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateTaskResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteTaskRequest, option: Optional[RequestOption] = None) -> DeleteTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteTaskResponse)
        response.raw = resp

        return response

    def get(self, request: GetTaskRequest, option: Optional[RequestOption] = None) -> GetTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), GetTaskResponse)
        response.raw = resp

        return response

    def list(self, request: ListTaskRequest, option: Optional[RequestOption] = None) -> ListTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), ListTaskResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchTaskRequest, option: Optional[RequestOption] = None) -> PatchTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchTaskResponse)
        response.raw = resp

        return response

    def uncomplete(self, request: UncompleteTaskRequest,
                   option: Optional[RequestOption] = None) -> UncompleteTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UncompleteTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), UncompleteTaskResponse)
        response.raw = resp

        return response
