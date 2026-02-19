from app.domain.models import Citation


class MockLLM:
    def generate_answer(self, question: str, citations: list[Citation]) -> str:
        if not citations:
            return "Insufficient evidence to provide an answer."
        refs = ", ".join(f"{c.doc_id}:{c.section}" for c in citations[:2])
        return f"Based on policy evidence, answer to '{question}' is supported by {refs}."
