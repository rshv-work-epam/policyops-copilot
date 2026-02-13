from app.application.agent import run_chat


def test_answer_includes_citations() -> None:
    resp = run_chat("How long should we retain financial records?", "general")
    assert resp.citations


def test_no_answer_when_retrieval_empty() -> None:
    resp = run_chat("zzzxxyyq unknown nonsense", "general")
    if not resp.citations:
        assert "could not find enough" in resp.answer.lower()


def test_approval_routing_restricted() -> None:
    resp = run_chat("Can I grant root access?", "information_security")
    assert resp.requires_approval is True
