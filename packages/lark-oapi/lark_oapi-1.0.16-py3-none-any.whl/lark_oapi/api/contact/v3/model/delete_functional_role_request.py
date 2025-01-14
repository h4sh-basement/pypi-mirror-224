# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteFunctionalRoleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.role_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteFunctionalRoleRequestBuilder":
        return DeleteFunctionalRoleRequestBuilder()


class DeleteFunctionalRoleRequestBuilder(object):

    def __init__(self) -> None:
        delete_functional_role_request = DeleteFunctionalRoleRequest()
        delete_functional_role_request.http_method = HttpMethod.DELETE
        delete_functional_role_request.uri = "/open-apis/contact/v3/functional_roles/:role_id"
        delete_functional_role_request.token_types = {AccessTokenType.TENANT}
        self._delete_functional_role_request: DeleteFunctionalRoleRequest = delete_functional_role_request

    def role_id(self, role_id: str) -> "DeleteFunctionalRoleRequestBuilder":
        self._delete_functional_role_request.role_id = role_id
        self._delete_functional_role_request.paths["role_id"] = str(role_id)
        return self

    def build(self) -> DeleteFunctionalRoleRequest:
        return self._delete_functional_role_request
