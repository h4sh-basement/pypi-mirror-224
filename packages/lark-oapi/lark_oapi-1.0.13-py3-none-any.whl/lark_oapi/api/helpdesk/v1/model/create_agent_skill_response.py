# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_agent_skill_response_body import CreateAgentSkillResponseBody


class CreateAgentSkillResponse(BaseResponse):
    _types = {
        "data": CreateAgentSkillResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateAgentSkillResponseBody] = None
        init(self, d, self._types)
