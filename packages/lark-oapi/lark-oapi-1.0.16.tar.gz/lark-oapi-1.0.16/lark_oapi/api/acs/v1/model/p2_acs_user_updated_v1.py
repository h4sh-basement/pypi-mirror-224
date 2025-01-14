# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2AcsUserUpdatedV1Data(object):
    _types = {
        "user_id": UserId,
        "card": int,
        "face_uploaded": bool,
    }

    def __init__(self, d=None):
        self.user_id: Optional[UserId] = None
        self.card: Optional[int] = None
        self.face_uploaded: Optional[bool] = None
        init(self, d, self._types)


class P2AcsUserUpdatedV1(EventContext):
    _types = {
        "event": P2AcsUserUpdatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2AcsUserUpdatedV1Data] = None
        init(self, d, self._types)
