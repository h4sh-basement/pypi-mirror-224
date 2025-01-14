# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserOrder(object):
    _types = {
        "department_id": str,
        "user_order": int,
        "department_order": int,
        "is_primary_dept": bool,
    }

    def __init__(self, d=None):
        self.department_id: Optional[str] = None
        self.user_order: Optional[int] = None
        self.department_order: Optional[int] = None
        self.is_primary_dept: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOrderBuilder":
        return UserOrderBuilder()


class UserOrderBuilder(object):
    def __init__(self) -> None:
        self._user_order = UserOrder()

    def department_id(self, department_id: str) -> "UserOrderBuilder":
        self._user_order.department_id = department_id
        return self

    def user_order(self, user_order: int) -> "UserOrderBuilder":
        self._user_order.user_order = user_order
        return self

    def department_order(self, department_order: int) -> "UserOrderBuilder":
        self._user_order.department_order = department_order
        return self

    def is_primary_dept(self, is_primary_dept: bool) -> "UserOrderBuilder":
        self._user_order.is_primary_dept = is_primary_dept
        return self

    def build(self) -> "UserOrder":
        return self._user_order
