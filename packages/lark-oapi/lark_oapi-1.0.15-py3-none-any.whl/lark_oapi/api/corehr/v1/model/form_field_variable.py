# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .bpm_dataengine_i18n import BpmDataengineI18n
from .form_variable_value_info import FormVariableValueInfo


class FormFieldVariable(object):
    _types = {
        "variable_api_name": str,
        "variable_name": BpmDataengineI18n,
        "variable_value": FormVariableValueInfo,
    }

    def __init__(self, d=None):
        self.variable_api_name: Optional[str] = None
        self.variable_name: Optional[BpmDataengineI18n] = None
        self.variable_value: Optional[FormVariableValueInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableBuilder":
        return FormFieldVariableBuilder()


class FormFieldVariableBuilder(object):
    def __init__(self) -> None:
        self._form_field_variable = FormFieldVariable()

    def variable_api_name(self, variable_api_name: str) -> "FormFieldVariableBuilder":
        self._form_field_variable.variable_api_name = variable_api_name
        return self

    def variable_name(self, variable_name: BpmDataengineI18n) -> "FormFieldVariableBuilder":
        self._form_field_variable.variable_name = variable_name
        return self

    def variable_value(self, variable_value: FormVariableValueInfo) -> "FormFieldVariableBuilder":
        self._form_field_variable.variable_value = variable_value
        return self

    def build(self) -> "FormFieldVariable":
        return self._form_field_variable
