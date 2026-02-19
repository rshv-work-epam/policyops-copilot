from datetime import datetime, timezone
import json

from sqlalchemy.orm import Session

from app.application.agent import run_chat
from app.domain.models import ApprovalRequest, ProcedureStepRequest
from app.infrastructure.db.models import Approval, AuditLog


PROCEDURES = {
    "Employee Expense Reimbursement": [
        "Collect receipts and verify policy limits.",
        "Submit expense report in finance portal.",
        "Attach manager approval and tax evidence.",
        "Finance review and payout confirmation.",
    ]
}


class PolicyService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def chat(self, question: str, category: str, actor: str, correlation_id: str):
        response = run_chat(question, category)
        self._audit(actor, "chat", {"question": question, "response": response.model_dump()}, correlation_id)
        return response

    def start_procedure(self, procedure_name: str) -> dict:
        steps = PROCEDURES.get(procedure_name, [])
        return {"procedure_name": procedure_name, "steps": steps, "current_step": 0}

    def next_step(self, req: ProcedureStepRequest) -> dict:
        steps = PROCEDURES.get(req.procedure_name, [])
        idx = min(req.current_step + 1, len(steps))
        return {"next_step": idx, "step_text": steps[idx - 1] if idx else "", "required_evidence": list(req.form_data.keys())}

    def create_approval(self, req: ApprovalRequest, actor: str, correlation_id: str) -> Approval:
        row = Approval(
            requester=actor,
            category=req.category,
            proposal=req.proposal,
            status="pending",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        self._audit(actor, "approval_request", {"id": row.id, "category": row.category}, correlation_id)
        return row

    def _audit(self, actor: str, action: str, payload: dict, correlation_id: str) -> None:
        self.db.add(
            AuditLog(
                actor=actor,
                action=action,
                payload=json.dumps(payload),
                correlation_id=correlation_id,
                created_at=datetime.now(timezone.utc),
            )
        )
        self.db.commit()
