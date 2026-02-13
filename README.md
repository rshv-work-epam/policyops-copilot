# PolicyOps Copilot

Azure-first, enterprise-style GenAI assistant for grounded policy Q/A, guided procedures, and human approvals with audit trail.

## Quick demo (local, no Azure)
1. `cp .env.example .env`
2. `docker compose up --build`
3. API health: `http://localhost:8000/health`
4. Web UI: `http://localhost:3000`

## Features
- Ask Policy with citations + confidence signals.
- Guided procedure wizard (Expense Reimbursement).
- Approval workflow with admin dashboard + audit logs.
- LangGraph state machine: classify -> retrieve -> draft -> self-check -> decide.
- Local fallbacks: mock auth, mock LLM, local retrieval.

## Azure switch-over
Set in `.env`:
- `LLM_PROVIDER=azure_openai`
- `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, deployment names.
- `VECTOR_BACKEND=azure_search` to use Azure AI Search adapter.

See docs:
- `docs/architecture.md`
- `docs/well_architected.md`
- `docs/runbook.md`
- `docs/threat_model.md`

## Manual Azure setup (exact)
1. Provision infra with `infra/terraform`.
2. Create Azure OpenAI resource/deployments (`gpt-4o-mini`, `text-embedding-3-small`) or point env vars to existing deployments.
3. Store secrets in Key Vault and inject into Container Apps env refs.
4. Enable Entra ID and switch `AUTH_MODE=entra` (validation adapter to be connected using documented JWT settings).

## Screenshots
Placeholders:
- `docs/screenshots/chat.png`
- `docs/screenshots/approval-dashboard.png`
