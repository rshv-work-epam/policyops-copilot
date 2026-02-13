from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.application.services import PolicyService
from app.domain.models import ApprovalDecision, ApprovalRequest
from app.infrastructure.auth.auth import Identity, get_identity
from app.infrastructure.db.models import Approval, AuditLog
from app.infrastructure.db.session import get_db

router = APIRouter(prefix="/api")


@router.post("/approvals/request")
def approval_request(req: dict, identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    parsed = ApprovalRequest(category=req.get("category", "general"), proposal=req.get("proposal", ""))
    return PolicyService(db).create_approval(parsed, identity.user_id, "approval-flow")


@router.get("/admin/approvals")
def list_approvals(identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    if identity.role != "admin":
        raise HTTPException(status_code=403, detail="Admin required")
    return db.query(Approval).order_by(Approval.created_at.desc()).all()


@router.post("/admin/approvals/{approval_id}/approve")
def approve(approval_id: int, req: dict, identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    row = db.get(Approval, approval_id)
    if not row:
        raise HTTPException(status_code=404, detail="Not found")
    parsed = ApprovalDecision(decision_notes=req.get("decision_notes", ""))
    row.status = "approved"
    row.reviewer = identity.user_id
    row.decision_notes = parsed.decision_notes
    row.updated_at = datetime.now(timezone.utc)
    db.add(row)
    db.add(AuditLog(actor=identity.user_id, action="approval_approved", payload=str(approval_id), correlation_id="admin", created_at=datetime.now(timezone.utc)))
    db.commit()
    return row


@router.post("/admin/approvals/{approval_id}/reject")
def reject(approval_id: int, req: dict, identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    row = db.get(Approval, approval_id)
    if not row:
        raise HTTPException(status_code=404, detail="Not found")
    parsed = ApprovalDecision(decision_notes=req.get("decision_notes", ""))
    row.status = "rejected"
    row.reviewer = identity.user_id
    row.decision_notes = parsed.decision_notes
    row.updated_at = datetime.now(timezone.utc)
    db.add(row)
    db.commit()
    return row


@router.get("/admin/audit-logs")
def audit_logs(identity: Identity = Depends(get_identity), db: Session = Depends(get_db)):
    if identity.role != "admin":
        raise HTTPException(status_code=403, detail="Admin required")
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).limit(200).all()
