# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class SubscriptionCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None

    @staticmethod
    def builder() -> "SubscriptionCalendarEventRequestBuilder":
        return SubscriptionCalendarEventRequestBuilder()


class SubscriptionCalendarEventRequestBuilder(object):

    def __init__(self) -> None:
        subscription_calendar_event_request = SubscriptionCalendarEventRequest()
        subscription_calendar_event_request.http_method = HttpMethod.POST
        subscription_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/subscription"
        subscription_calendar_event_request.token_types = {AccessTokenType.USER}
        self._subscription_calendar_event_request: SubscriptionCalendarEventRequest = subscription_calendar_event_request

    def calendar_id(self, calendar_id: str) -> "SubscriptionCalendarEventRequestBuilder":
        self._subscription_calendar_event_request.calendar_id = calendar_id
        self._subscription_calendar_event_request.paths["calendar_id"] = str(calendar_id)
        return self

    def build(self) -> SubscriptionCalendarEventRequest:
        return self._subscription_calendar_event_request
