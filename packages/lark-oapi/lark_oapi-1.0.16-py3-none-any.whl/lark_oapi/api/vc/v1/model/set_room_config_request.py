# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .set_room_config_request_body import SetRoomConfigRequestBody


class SetRoomConfigRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[SetRoomConfigRequestBody] = None

    @staticmethod
    def builder() -> "SetRoomConfigRequestBuilder":
        return SetRoomConfigRequestBuilder()


class SetRoomConfigRequestBuilder(object):

    def __init__(self) -> None:
        set_room_config_request = SetRoomConfigRequest()
        set_room_config_request.http_method = HttpMethod.POST
        set_room_config_request.uri = "/open-apis/vc/v1/room_configs/set"
        set_room_config_request.token_types = {AccessTokenType.TENANT}
        self._set_room_config_request: SetRoomConfigRequest = set_room_config_request

    def user_id_type(self, user_id_type: str) -> "SetRoomConfigRequestBuilder":
        self._set_room_config_request.user_id_type = user_id_type
        self._set_room_config_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: SetRoomConfigRequestBody) -> "SetRoomConfigRequestBuilder":
        self._set_room_config_request.request_body = request_body
        self._set_room_config_request.body = request_body
        return self

    def build(self) -> SetRoomConfigRequest:
        return self._set_room_config_request
