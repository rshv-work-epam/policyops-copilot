from collections import defaultdict
from datetime import datetime, timedelta


class InMemoryRateLimiter:
    def __init__(self, limit_per_minute: int) -> None:
        self.limit = limit_per_minute
        self.events: dict[str, list[datetime]] = defaultdict(list)

    def allowed(self, key: str) -> bool:
        now = datetime.utcnow()
        window = now - timedelta(minutes=1)
        kept = [ts for ts in self.events[key] if ts > window]
        kept.append(now)
        self.events[key] = kept
        return len(kept) <= self.limit
