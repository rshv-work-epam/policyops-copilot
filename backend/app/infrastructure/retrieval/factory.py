from functools import lru_cache

from app.core.config import settings
from app.infrastructure.retrieval.azure_search_retriever import AzureSearchRetriever
from app.infrastructure.retrieval.faiss_retriever import LocalRetriever


@lru_cache(maxsize=1)
def get_retriever():
    if settings.vector_backend == "azure_search":
        return AzureSearchRetriever()
    return LocalRetriever()
