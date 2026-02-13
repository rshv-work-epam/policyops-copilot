from typing import Protocol

from app.domain.models import Citation


class Retriever(Protocol):
    def query(self, question: str, top_k: int) -> list[Citation]: ...


class LLMClient(Protocol):
    def generate_answer(self, question: str, citations: list[Citation]) -> str: ...


class ApprovalRepository(Protocol):
    ...
