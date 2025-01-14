# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetCalendarRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCalendarRequestBuilder":
        return GetCalendarRequestBuilder()


class GetCalendarRequestBuilder(object):

    def __init__(self) -> None:
        get_calendar_request = GetCalendarRequest()
        get_calendar_request.http_method = HttpMethod.GET
        get_calendar_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id"
        get_calendar_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_calendar_request: GetCalendarRequest = get_calendar_request

    def calendar_id(self, calendar_id: str) -> "GetCalendarRequestBuilder":
        self._get_calendar_request.calendar_id = calendar_id
        self._get_calendar_request.paths["calendar_id"] = str(calendar_id)
        return self

    def build(self) -> GetCalendarRequest:
        return self._get_calendar_request
