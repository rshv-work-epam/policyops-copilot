from fastapi import APIRouter

from scripts.ingest import run_ingestion

router = APIRouter(prefix="/api/admin")


@router.post("/ingest")
def ingest() -> dict[str, str]:
    run_ingestion()
    return {"status": "ingestion_completed"}
