# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .upload_part_file_request_body import UploadPartFileRequestBody


class UploadPartFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UploadPartFileRequestBody] = None

    @staticmethod
    def builder() -> "UploadPartFileRequestBuilder":
        return UploadPartFileRequestBuilder()


class UploadPartFileRequestBuilder(object):

    def __init__(self) -> None:
        upload_part_file_request = UploadPartFileRequest()
        upload_part_file_request.http_method = HttpMethod.POST
        upload_part_file_request.uri = "/open-apis/drive/v1/files/upload_part"
        upload_part_file_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._upload_part_file_request: UploadPartFileRequest = upload_part_file_request

    def request_body(self, request_body: UploadPartFileRequestBody) -> "UploadPartFileRequestBuilder":
        self._upload_part_file_request.request_body = request_body
        self._upload_part_file_request.body = request_body
        return self

    def build(self) -> UploadPartFileRequest:
        return self._upload_part_file_request
