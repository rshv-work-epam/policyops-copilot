from pathlib import Path
import re

from app.core.config import settings
from app.domain.models import Citation


class LocalRetriever:
    def __init__(self) -> None:
        self.docs: list[tuple[str, str, str]] = []
        data_path = Path(settings.policy_data_path)
        for fp in data_path.glob("*.md"):
            text = fp.read_text()
            sections = re.split(r"\n## ", text)
            for sec in sections:
                title = sec.splitlines()[0][:120] if sec else "section"
                self.docs.append((fp.stem, title, sec[:600]))

    def _score(self, q: str, text: str) -> float:
        q_terms = set(re.findall(r"[a-zA-Z]+", q.lower()))
        t_terms = set(re.findall(r"[a-zA-Z]+", text.lower()))
        if not q_terms:
            return 0.0
        return len(q_terms & t_terms) / len(q_terms)

    def query(self, question: str, top_k: int) -> list[Citation]:
        ranked = sorted(
            [(i, self._score(question, d[2])) for i, d in enumerate(self.docs)],
            key=lambda x: x[1],
            reverse=True,
        )[:top_k]
        return [
            Citation(doc_id=self.docs[i][0], section=self.docs[i][1], snippet=self.docs[i][2][:200], score=float(s))
            for i, s in ranked
            if s > 0.05
        ]
