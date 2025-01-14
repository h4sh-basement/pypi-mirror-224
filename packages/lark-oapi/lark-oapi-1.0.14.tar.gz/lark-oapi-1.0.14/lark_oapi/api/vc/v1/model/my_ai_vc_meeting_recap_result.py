# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MyAiVcMeetingRecapResult(object):
    _types = {
        "meeting_recap_or_fail_reason": str,
        "meeting_recap": str,
    }

    def __init__(self, d=None):
        self.meeting_recap_or_fail_reason: Optional[str] = None
        self.meeting_recap: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiVcMeetingRecapResultBuilder":
        return MyAiVcMeetingRecapResultBuilder()


class MyAiVcMeetingRecapResultBuilder(object):
    def __init__(self) -> None:
        self._my_ai_vc_meeting_recap_result = MyAiVcMeetingRecapResult()

    def meeting_recap_or_fail_reason(self, meeting_recap_or_fail_reason: str) -> "MyAiVcMeetingRecapResultBuilder":
        self._my_ai_vc_meeting_recap_result.meeting_recap_or_fail_reason = meeting_recap_or_fail_reason
        return self

    def meeting_recap(self, meeting_recap: str) -> "MyAiVcMeetingRecapResultBuilder":
        self._my_ai_vc_meeting_recap_result.meeting_recap = meeting_recap
        return self

    def build(self) -> "MyAiVcMeetingRecapResult":
        return self._my_ai_vc_meeting_recap_result
