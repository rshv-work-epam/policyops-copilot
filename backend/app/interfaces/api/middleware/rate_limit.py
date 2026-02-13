from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.config import settings
from app.core.security import InMemoryRateLimiter


limiter = InMemoryRateLimiter(settings.rate_limit_per_minute)


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        key = request.headers.get("x-mock-user", "anonymous")
        if not limiter.allowed(key):
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
        return await call_next(request)
