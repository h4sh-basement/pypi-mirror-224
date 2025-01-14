# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2AcsAccessRecordCreatedV1Data(object):
    _types = {
        "access_record_id": str,
        "user_id": UserId,
        "device_id": str,
        "is_clock_in": bool,
        "is_door_open": bool,
        "access_time": str,
    }

    def __init__(self, d=None):
        self.access_record_id: Optional[str] = None
        self.user_id: Optional[UserId] = None
        self.device_id: Optional[str] = None
        self.is_clock_in: Optional[bool] = None
        self.is_door_open: Optional[bool] = None
        self.access_time: Optional[str] = None
        init(self, d, self._types)


class P2AcsAccessRecordCreatedV1(EventContext):
    _types = {
        "event": P2AcsAccessRecordCreatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2AcsAccessRecordCreatedV1Data] = None
        init(self, d, self._types)
