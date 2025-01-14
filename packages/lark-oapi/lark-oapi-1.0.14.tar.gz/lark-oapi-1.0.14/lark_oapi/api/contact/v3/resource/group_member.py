# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.add_group_member_request import AddGroupMemberRequest
from ..model.add_group_member_response import AddGroupMemberResponse
from ..model.batch_add_group_member_request import BatchAddGroupMemberRequest
from ..model.batch_add_group_member_response import BatchAddGroupMemberResponse
from ..model.batch_remove_group_member_request import BatchRemoveGroupMemberRequest
from ..model.batch_remove_group_member_response import BatchRemoveGroupMemberResponse
from ..model.remove_group_member_request import RemoveGroupMemberRequest
from ..model.remove_group_member_response import RemoveGroupMemberResponse
from ..model.simplelist_group_member_request import SimplelistGroupMemberRequest
from ..model.simplelist_group_member_response import SimplelistGroupMemberResponse


class GroupMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def add(self, request: AddGroupMemberRequest, option: Optional[RequestOption] = None) -> AddGroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: AddGroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), AddGroupMemberResponse)
        response.raw = resp

        return response

    def batch_add(self, request: BatchAddGroupMemberRequest,
                  option: Optional[RequestOption] = None) -> BatchAddGroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchAddGroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchAddGroupMemberResponse)
        response.raw = resp

        return response

    def batch_remove(self, request: BatchRemoveGroupMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchRemoveGroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchRemoveGroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  BatchRemoveGroupMemberResponse)
        response.raw = resp

        return response

    def remove(self, request: RemoveGroupMemberRequest,
               option: Optional[RequestOption] = None) -> RemoveGroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: RemoveGroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), RemoveGroupMemberResponse)
        response.raw = resp

        return response

    def simplelist(self, request: SimplelistGroupMemberRequest,
                   option: Optional[RequestOption] = None) -> SimplelistGroupMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SimplelistGroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 SimplelistGroupMemberResponse)
        response.raw = resp

        return response
