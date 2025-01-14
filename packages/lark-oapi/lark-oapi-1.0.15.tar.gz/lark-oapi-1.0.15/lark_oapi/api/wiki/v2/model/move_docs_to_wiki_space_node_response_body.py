# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MoveDocsToWikiSpaceNodeResponseBody(object):
    _types = {
        "wiki_token": str,
        "task_id": str,
        "applied": bool,
    }

    def __init__(self, d=None):
        self.wiki_token: Optional[str] = None
        self.task_id: Optional[str] = None
        self.applied: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MoveDocsToWikiSpaceNodeResponseBodyBuilder":
        return MoveDocsToWikiSpaceNodeResponseBodyBuilder()


class MoveDocsToWikiSpaceNodeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._move_docs_to_wiki_space_node_response_body = MoveDocsToWikiSpaceNodeResponseBody()

    def wiki_token(self, wiki_token: str) -> "MoveDocsToWikiSpaceNodeResponseBodyBuilder":
        self._move_docs_to_wiki_space_node_response_body.wiki_token = wiki_token
        return self

    def task_id(self, task_id: str) -> "MoveDocsToWikiSpaceNodeResponseBodyBuilder":
        self._move_docs_to_wiki_space_node_response_body.task_id = task_id
        return self

    def applied(self, applied: bool) -> "MoveDocsToWikiSpaceNodeResponseBodyBuilder":
        self._move_docs_to_wiki_space_node_response_body.applied = applied
        return self

    def build(self) -> "MoveDocsToWikiSpaceNodeResponseBody":
        return self._move_docs_to_wiki_space_node_response_body
