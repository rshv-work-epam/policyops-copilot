from uuid import uuid4
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.services import PolicyService
from app.infrastructure.auth.auth import Identity, get_identity
from app.infrastructure.db.session import get_db

router = APIRouter(prefix="/api")


@router.post("/chat")
def chat(req: dict, identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    service = PolicyService(db)
    return service.chat(req.get("question", ""), req.get("category", "general"), identity.user_id, str(uuid4()))
