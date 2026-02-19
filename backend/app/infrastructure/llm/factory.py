from app.core.config import settings
from app.infrastructure.llm.azure_openai_llm import AzureOpenAILLM
from app.infrastructure.llm.mock_llm import MockLLM


def get_llm_client():
    if settings.llm_provider == "azure_openai" and settings.azure_openai_api_key:
        return AzureOpenAILLM()
    return MockLLM()
