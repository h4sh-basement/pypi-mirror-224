# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class TicketImageTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_id: Optional[str] = None
        self.msg_id: Optional[str] = None
        self.index: Optional[int] = None

    @staticmethod
    def builder() -> "TicketImageTicketRequestBuilder":
        return TicketImageTicketRequestBuilder()


class TicketImageTicketRequestBuilder(object):

    def __init__(self) -> None:
        ticket_image_ticket_request = TicketImageTicketRequest()
        ticket_image_ticket_request.http_method = HttpMethod.GET
        ticket_image_ticket_request.uri = "/open-apis/helpdesk/v1/ticket_images"
        ticket_image_ticket_request.token_types = {AccessTokenType.TENANT}
        self._ticket_image_ticket_request: TicketImageTicketRequest = ticket_image_ticket_request

    def ticket_id(self, ticket_id: str) -> "TicketImageTicketRequestBuilder":
        self._ticket_image_ticket_request.ticket_id = ticket_id
        self._ticket_image_ticket_request.add_query("ticket_id", ticket_id)
        return self

    def msg_id(self, msg_id: str) -> "TicketImageTicketRequestBuilder":
        self._ticket_image_ticket_request.msg_id = msg_id
        self._ticket_image_ticket_request.add_query("msg_id", msg_id)
        return self

    def index(self, index: int) -> "TicketImageTicketRequestBuilder":
        self._ticket_image_ticket_request.index = index
        self._ticket_image_ticket_request.add_query("index", index)
        return self

    def build(self) -> TicketImageTicketRequest:
        return self._ticket_image_ticket_request
