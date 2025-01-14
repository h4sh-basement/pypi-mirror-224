# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .participant import Participant


class GetParticipantListResponseBody(object):
    _types = {
        "participants": List[Participant],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.participants: Optional[List[Participant]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetParticipantListResponseBodyBuilder":
        return GetParticipantListResponseBodyBuilder()


class GetParticipantListResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_participant_list_response_body = GetParticipantListResponseBody()

    def participants(self, participants: List[Participant]) -> "GetParticipantListResponseBodyBuilder":
        self._get_participant_list_response_body.participants = participants
        return self

    def page_token(self, page_token: str) -> "GetParticipantListResponseBodyBuilder":
        self._get_participant_list_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "GetParticipantListResponseBodyBuilder":
        self._get_participant_list_response_body.has_more = has_more
        return self

    def build(self) -> "GetParticipantListResponseBody":
        return self._get_participant_list_response_body
