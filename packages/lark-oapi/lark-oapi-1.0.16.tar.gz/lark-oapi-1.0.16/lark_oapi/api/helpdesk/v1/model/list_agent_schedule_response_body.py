# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .agent_schedule import AgentSchedule


class ListAgentScheduleResponseBody(object):
    _types = {
        "agent_schedules": List[AgentSchedule],
    }

    def __init__(self, d=None):
        self.agent_schedules: Optional[List[AgentSchedule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAgentScheduleResponseBodyBuilder":
        return ListAgentScheduleResponseBodyBuilder()


class ListAgentScheduleResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_agent_schedule_response_body = ListAgentScheduleResponseBody()

    def agent_schedules(self, agent_schedules: List[AgentSchedule]) -> "ListAgentScheduleResponseBodyBuilder":
        self._list_agent_schedule_response_body.agent_schedules = agent_schedules
        return self

    def build(self) -> "ListAgentScheduleResponseBody":
        return self._list_agent_schedule_response_body
