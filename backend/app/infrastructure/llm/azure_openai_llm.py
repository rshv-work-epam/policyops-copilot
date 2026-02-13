from app.domain.models import Citation


class AzureOpenAILLM:
    def generate_answer(self, question: str, citations: list[Citation]) -> str:
        # Minimal placeholder to keep local runtime independent from cloud credentials.
        joined = "; ".join(c.snippet[:50] for c in citations)
        return f"Azure OpenAI answer (placeholder) for '{question}' grounded in: {joined}"
