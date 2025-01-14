# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meeting_invite_status import MeetingInviteStatus


class InviteMeetingResponseBody(object):
    _types = {
        "invite_results": List[MeetingInviteStatus],
    }

    def __init__(self, d=None):
        self.invite_results: Optional[List[MeetingInviteStatus]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InviteMeetingResponseBodyBuilder":
        return InviteMeetingResponseBodyBuilder()


class InviteMeetingResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._invite_meeting_response_body = InviteMeetingResponseBody()

    def invite_results(self, invite_results: List[MeetingInviteStatus]) -> "InviteMeetingResponseBodyBuilder":
        self._invite_meeting_response_body.invite_results = invite_results
        return self

    def build(self) -> "InviteMeetingResponseBody":
        return self._invite_meeting_response_body
