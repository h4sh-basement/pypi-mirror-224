# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetParticipantQualityListRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_start_time: Optional[int] = None
        self.meeting_end_time: Optional[int] = None
        self.meeting_no: Optional[str] = None
        self.join_time: Optional[int] = None
        self.user_id: Optional[str] = None
        self.room_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "GetParticipantQualityListRequestBuilder":
        return GetParticipantQualityListRequestBuilder()


class GetParticipantQualityListRequestBuilder(object):

    def __init__(self) -> None:
        get_participant_quality_list_request = GetParticipantQualityListRequest()
        get_participant_quality_list_request.http_method = HttpMethod.GET
        get_participant_quality_list_request.uri = "/open-apis/vc/v1/participant_quality_list"
        get_participant_quality_list_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_participant_quality_list_request: GetParticipantQualityListRequest = get_participant_quality_list_request

    def meeting_start_time(self, meeting_start_time: int) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.meeting_start_time = meeting_start_time
        self._get_participant_quality_list_request.add_query("meeting_start_time", meeting_start_time)
        return self

    def meeting_end_time(self, meeting_end_time: int) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.meeting_end_time = meeting_end_time
        self._get_participant_quality_list_request.add_query("meeting_end_time", meeting_end_time)
        return self

    def meeting_no(self, meeting_no: str) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.meeting_no = meeting_no
        self._get_participant_quality_list_request.add_query("meeting_no", meeting_no)
        return self

    def join_time(self, join_time: int) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.join_time = join_time
        self._get_participant_quality_list_request.add_query("join_time", join_time)
        return self

    def user_id(self, user_id: str) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.user_id = user_id
        self._get_participant_quality_list_request.add_query("user_id", user_id)
        return self

    def room_id(self, room_id: str) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.room_id = room_id
        self._get_participant_quality_list_request.add_query("room_id", room_id)
        return self

    def page_size(self, page_size: int) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.page_size = page_size
        self._get_participant_quality_list_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.page_token = page_token
        self._get_participant_quality_list_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "GetParticipantQualityListRequestBuilder":
        self._get_participant_quality_list_request.user_id_type = user_id_type
        self._get_participant_quality_list_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> GetParticipantQualityListRequest:
        return self._get_participant_quality_list_request
