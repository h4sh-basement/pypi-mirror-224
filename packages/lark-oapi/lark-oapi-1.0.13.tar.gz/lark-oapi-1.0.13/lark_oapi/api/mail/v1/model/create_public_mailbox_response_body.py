# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreatePublicMailboxResponseBody(object):
    _types = {
        "public_mailbox_id": str,
        "email": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.public_mailbox_id: Optional[str] = None
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePublicMailboxResponseBodyBuilder":
        return CreatePublicMailboxResponseBodyBuilder()


class CreatePublicMailboxResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_public_mailbox_response_body = CreatePublicMailboxResponseBody()

    def public_mailbox_id(self, public_mailbox_id: str) -> "CreatePublicMailboxResponseBodyBuilder":
        self._create_public_mailbox_response_body.public_mailbox_id = public_mailbox_id
        return self

    def email(self, email: str) -> "CreatePublicMailboxResponseBodyBuilder":
        self._create_public_mailbox_response_body.email = email
        return self

    def name(self, name: str) -> "CreatePublicMailboxResponseBodyBuilder":
        self._create_public_mailbox_response_body.name = name
        return self

    def build(self) -> "CreatePublicMailboxResponseBody":
        return self._create_public_mailbox_response_body
