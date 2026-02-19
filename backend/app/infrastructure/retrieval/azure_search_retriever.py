from app.domain.models import Citation


class AzureSearchRetriever:
    def query(self, question: str, top_k: int) -> list[Citation]:
        return [
            Citation(
                doc_id="azure-search-placeholder",
                section="sample",
                snippet=f"Configure Azure AI Search integration for: {question}",
                score=0.9,
            )
        ][:top_k]
