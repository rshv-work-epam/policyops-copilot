from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app.core.logging import configure_logging
from app.infrastructure.observability.tracing import configure_tracing
from app.interfaces.api.middleware.rate_limit import RateLimitMiddleware
from app.interfaces.api.routes import approvals, chat, health, ingest, procedure

configure_logging()
configure_tracing()

app = FastAPI(title="PolicyOps Copilot API")
app.add_middleware(RateLimitMiddleware)
app.include_router(health.router)
app.include_router(chat.router)
app.include_router(procedure.router)
app.include_router(approvals.router)
app.include_router(ingest.router)
FastAPIInstrumentor.instrument_app(app)
