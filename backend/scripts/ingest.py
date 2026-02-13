from pathlib import Path

from app.core.config import settings


def run_ingestion() -> None:
    path = Path(settings.policy_data_path)
    if not path.exists():
        raise FileNotFoundError(f"Missing policy path: {path}")
    # Retrieval is file-backed TF-IDF in MVP; touching files is enough.
    _ = [p.name for p in path.glob("*.md")]


if __name__ == "__main__":
    run_ingestion()
    print("Ingestion complete")
