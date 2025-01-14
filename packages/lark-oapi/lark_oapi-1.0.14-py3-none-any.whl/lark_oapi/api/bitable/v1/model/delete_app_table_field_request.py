# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteAppTableFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.field_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAppTableFieldRequestBuilder":
        return DeleteAppTableFieldRequestBuilder()


class DeleteAppTableFieldRequestBuilder(object):

    def __init__(self) -> None:
        delete_app_table_field_request = DeleteAppTableFieldRequest()
        delete_app_table_field_request.http_method = HttpMethod.DELETE
        delete_app_table_field_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields/:field_id"
        delete_app_table_field_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_app_table_field_request: DeleteAppTableFieldRequest = delete_app_table_field_request

    def app_token(self, app_token: str) -> "DeleteAppTableFieldRequestBuilder":
        self._delete_app_table_field_request.app_token = app_token
        self._delete_app_table_field_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "DeleteAppTableFieldRequestBuilder":
        self._delete_app_table_field_request.table_id = table_id
        self._delete_app_table_field_request.paths["table_id"] = str(table_id)
        return self

    def field_id(self, field_id: str) -> "DeleteAppTableFieldRequestBuilder":
        self._delete_app_table_field_request.field_id = field_id
        self._delete_app_table_field_request.paths["field_id"] = str(field_id)
        return self

    def build(self) -> DeleteAppTableFieldRequest:
        return self._delete_app_table_field_request
