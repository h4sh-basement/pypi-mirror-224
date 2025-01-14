# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .emoji import Emoji
from .user_id import UserId


class P2ImMessageReactionDeletedV1Data(object):
    _types = {
        "message_id": str,
        "reaction_type": Emoji,
        "operator_type": str,
        "user_id": UserId,
        "app_id": str,
        "action_time": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.reaction_type: Optional[Emoji] = None
        self.operator_type: Optional[str] = None
        self.user_id: Optional[UserId] = None
        self.app_id: Optional[str] = None
        self.action_time: Optional[str] = None
        init(self, d, self._types)


class P2ImMessageReactionDeletedV1(EventContext):
    _types = {
        "event": P2ImMessageReactionDeletedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ImMessageReactionDeletedV1Data] = None
        init(self, d, self._types)
