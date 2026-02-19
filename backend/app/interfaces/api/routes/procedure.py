from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.services import PolicyService
from app.domain.models import ProcedureStepRequest
from app.infrastructure.db.session import get_db

router = APIRouter(prefix="/api/procedure")


@router.post("/start")
def start(req: dict, db: Session = Depends(get_db)):
    return PolicyService(db).start_procedure(req.get("procedure_name", ""))


@router.post("/step")
def step(req: dict, db: Session = Depends(get_db)):
    parsed = ProcedureStepRequest(
        procedure_name=req.get("procedure_name", ""),
        current_step=req.get("current_step", 0),
        form_data=req.get("form_data", {}),
    )
    return PolicyService(db).next_step(parsed)
