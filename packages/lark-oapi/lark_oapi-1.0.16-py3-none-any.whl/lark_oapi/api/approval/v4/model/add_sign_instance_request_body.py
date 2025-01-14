# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddSignInstanceRequestBody(object):
    _types = {
        "user_id": str,
        "approval_code": str,
        "instance_code": str,
        "task_id": str,
        "comment": str,
        "add_sign_user_ids": List[str],
        "add_sign_type": int,
        "approval_method": int,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.task_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.add_sign_user_ids: Optional[List[str]] = None
        self.add_sign_type: Optional[int] = None
        self.approval_method: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddSignInstanceRequestBodyBuilder":
        return AddSignInstanceRequestBodyBuilder()


class AddSignInstanceRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_sign_instance_request_body = AddSignInstanceRequestBody()

    def user_id(self, user_id: str) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.user_id = user_id
        return self

    def approval_code(self, approval_code: str) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.approval_code = approval_code
        return self

    def instance_code(self, instance_code: str) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.instance_code = instance_code
        return self

    def task_id(self, task_id: str) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.task_id = task_id
        return self

    def comment(self, comment: str) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.comment = comment
        return self

    def add_sign_user_ids(self, add_sign_user_ids: List[str]) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.add_sign_user_ids = add_sign_user_ids
        return self

    def add_sign_type(self, add_sign_type: int) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.add_sign_type = add_sign_type
        return self

    def approval_method(self, approval_method: int) -> "AddSignInstanceRequestBodyBuilder":
        self._add_sign_instance_request_body.approval_method = approval_method
        return self

    def build(self) -> "AddSignInstanceRequestBody":
        return self._add_sign_instance_request_body
