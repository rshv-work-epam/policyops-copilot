from dataclasses import dataclass, asdict


@dataclass
class Citation:
    doc_id: str
    section: str
    snippet: str
    score: float


@dataclass
class ChatRequest:
    question: str
    category: str = "general"


@dataclass
class ChatResponse:
    answer: str
    citations: list[Citation]
    retrieval_score_band: str
    citation_coverage: float
    requires_approval: bool = False

    def model_dump(self):
        return asdict(self)


@dataclass
class ProcedureStartRequest:
    procedure_name: str


@dataclass
class ProcedureStepRequest:
    procedure_name: str
    current_step: int
    form_data: dict[str, str]


@dataclass
class ApprovalRequest:
    category: str
    proposal: str


@dataclass
class ApprovalDecision:
    decision_notes: str = ""
