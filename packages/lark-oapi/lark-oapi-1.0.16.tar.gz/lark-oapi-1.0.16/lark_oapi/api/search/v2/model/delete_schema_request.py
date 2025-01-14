# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteSchemaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.schema_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteSchemaRequestBuilder":
        return DeleteSchemaRequestBuilder()


class DeleteSchemaRequestBuilder(object):

    def __init__(self) -> None:
        delete_schema_request = DeleteSchemaRequest()
        delete_schema_request.http_method = HttpMethod.DELETE
        delete_schema_request.uri = "/open-apis/search/v2/schemas/:schema_id"
        delete_schema_request.token_types = {AccessTokenType.TENANT}
        self._delete_schema_request: DeleteSchemaRequest = delete_schema_request

    def schema_id(self, schema_id: str) -> "DeleteSchemaRequestBuilder":
        self._delete_schema_request.schema_id = schema_id
        self._delete_schema_request.paths["schema_id"] = str(schema_id)
        return self

    def build(self) -> DeleteSchemaRequest:
        return self._delete_schema_request
