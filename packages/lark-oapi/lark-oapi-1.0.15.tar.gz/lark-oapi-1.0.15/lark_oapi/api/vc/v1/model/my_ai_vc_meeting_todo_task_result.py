# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MyAiVcMeetingTodoTaskResult(object):
    _types = {
        "meeting_todo_task_or_fail_reason": str,
        "meeting_todo_task": str,
    }

    def __init__(self, d=None):
        self.meeting_todo_task_or_fail_reason: Optional[str] = None
        self.meeting_todo_task: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiVcMeetingTodoTaskResultBuilder":
        return MyAiVcMeetingTodoTaskResultBuilder()


class MyAiVcMeetingTodoTaskResultBuilder(object):
    def __init__(self) -> None:
        self._my_ai_vc_meeting_todo_task_result = MyAiVcMeetingTodoTaskResult()

    def meeting_todo_task_or_fail_reason(self,
                                         meeting_todo_task_or_fail_reason: str) -> "MyAiVcMeetingTodoTaskResultBuilder":
        self._my_ai_vc_meeting_todo_task_result.meeting_todo_task_or_fail_reason = meeting_todo_task_or_fail_reason
        return self

    def meeting_todo_task(self, meeting_todo_task: str) -> "MyAiVcMeetingTodoTaskResultBuilder":
        self._my_ai_vc_meeting_todo_task_result.meeting_todo_task = meeting_todo_task
        return self

    def build(self) -> "MyAiVcMeetingTodoTaskResult":
        return self._my_ai_vc_meeting_todo_task_result
