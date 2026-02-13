from typing import Literal, TypedDict

from langgraph.graph import END, StateGraph

from app.core.config import settings
from app.domain.models import ChatResponse, Citation
from app.infrastructure.llm.factory import get_llm_client
from app.infrastructure.retrieval.factory import get_retriever


class AgentState(TypedDict, total=False):
    question: str
    category: str
    intent: Literal["qa", "procedure", "approval"]
    citations: list[Citation]
    answer: str
    citation_coverage: float
    decision: Literal["answer", "clarify", "approval"]


def classify(state: AgentState) -> AgentState:
    cat = state.get("category", "general")
    if cat in settings.restricted_categories.split(","):
        state["intent"] = "approval"
    else:
        state["intent"] = "qa"
    return state


def retrieve(state: AgentState) -> AgentState:
    retriever = get_retriever()
    state["citations"] = retriever.query(state["question"], settings.top_k)
    return state


def draft(state: AgentState) -> AgentState:
    llm = get_llm_client()
    citations = state.get("citations", [])
    state["answer"] = llm.generate_answer(state["question"], citations)
    return state


def self_check(state: AgentState) -> AgentState:
    citations = state.get("citations", [])
    coverage = min(1.0, len(citations) / max(1, settings.top_k))
    state["citation_coverage"] = coverage
    if state.get("intent") == "approval":
        state["decision"] = "approval"
    elif coverage < settings.min_citation_coverage:
        state["decision"] = "clarify"
    else:
        state["decision"] = "answer"
    return state


def route(state: AgentState) -> str:
    return state.get("decision", "clarify")


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("classify", classify)
    graph.add_node("retrieve", retrieve)
    graph.add_node("draft", draft)
    graph.add_node("self_check", self_check)

    graph.set_entry_point("classify")
    graph.add_edge("classify", "retrieve")
    graph.add_edge("retrieve", "draft")
    graph.add_edge("draft", "self_check")
    graph.add_conditional_edges("self_check", route, {"answer": END, "clarify": END, "approval": END})
    return graph.compile()


def run_chat(question: str, category: str = "general") -> ChatResponse:
    app = build_graph()
    result = app.invoke({"question": question, "category": category})
    decision = result.get("decision", "clarify")
    citations = result.get("citations", [])
    band = "high" if citations and citations[0].score > 0.75 else "medium" if citations else "low"
    if decision == "clarify":
        answer = "I could not find enough grounded evidence. Please clarify your question or provide more context."
    else:
        answer = result.get("answer", "")
    return ChatResponse(
        answer=answer,
        citations=citations,
        retrieval_score_band=band,
        citation_coverage=result.get("citation_coverage", 0.0),
        requires_approval=decision == "approval",
    )
