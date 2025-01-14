# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .filter_view_condition import FilterViewCondition


class UpdateSpreadsheetSheetFilterViewConditionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None
        self.condition_id: Optional[str] = None
        self.request_body: Optional[FilterViewCondition] = None

    @staticmethod
    def builder() -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        return UpdateSpreadsheetSheetFilterViewConditionRequestBuilder()


class UpdateSpreadsheetSheetFilterViewConditionRequestBuilder(object):

    def __init__(self) -> None:
        update_spreadsheet_sheet_filter_view_condition_request = UpdateSpreadsheetSheetFilterViewConditionRequest()
        update_spreadsheet_sheet_filter_view_condition_request.http_method = HttpMethod.PUT
        update_spreadsheet_sheet_filter_view_condition_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id"
        update_spreadsheet_sheet_filter_view_condition_request.token_types = {AccessTokenType.TENANT,
                                                                              AccessTokenType.USER}
        self._update_spreadsheet_sheet_filter_view_condition_request: UpdateSpreadsheetSheetFilterViewConditionRequest = update_spreadsheet_sheet_filter_view_condition_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_request.spreadsheet_token = spreadsheet_token
        self._update_spreadsheet_sheet_filter_view_condition_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_request.sheet_id = sheet_id
        self._update_spreadsheet_sheet_filter_view_condition_request.paths["sheet_id"] = str(sheet_id)
        return self

    def filter_view_id(self, filter_view_id: str) -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_request.filter_view_id = filter_view_id
        self._update_spreadsheet_sheet_filter_view_condition_request.paths["filter_view_id"] = str(filter_view_id)
        return self

    def condition_id(self, condition_id: str) -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_request.condition_id = condition_id
        self._update_spreadsheet_sheet_filter_view_condition_request.paths["condition_id"] = str(condition_id)
        return self

    def request_body(self,
                     request_body: FilterViewCondition) -> "UpdateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_request.request_body = request_body
        self._update_spreadsheet_sheet_filter_view_condition_request.body = request_body
        return self

    def build(self) -> UpdateSpreadsheetSheetFilterViewConditionRequest:
        return self._update_spreadsheet_sheet_filter_view_condition_request
