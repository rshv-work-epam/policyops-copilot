import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "local")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg://policyops:policyops@postgres:5432/policyops")
    auth_mode: str = os.getenv("AUTH_MODE", "mock")
    mock_default_role: str = os.getenv("MOCK_DEFAULT_ROLE", "admin")
    mock_default_user: str = os.getenv("MOCK_DEFAULT_USER", "demo.user")
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    restricted_categories: str = os.getenv("RESTRICTED_CATEGORIES", "information_security,access_management")
    vector_backend: str = os.getenv("VECTOR_BACKEND", "faiss")
    faiss_index_path: str = os.getenv("FAISS_INDEX_PATH", "/app/.faiss/index")
    policy_data_path: str = os.getenv("POLICY_DATA_PATH", "../data/sample_policies")
    top_k: int = int(os.getenv("TOP_K", "4"))
    min_citation_coverage: float = float(os.getenv("MIN_CITATION_COVERAGE", "0.6"))
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    azure_openai_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    azure_openai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    azure_openai_chat_deployment: str = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "gpt-4o-mini")
    azure_openai_embedding_deployment: str = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
    azure_openai_api_version: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")


settings = Settings()
