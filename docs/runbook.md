# Runbook
## Checks
- API: `curl localhost:8000/health`
- DB connectivity: inspect API logs for SQL errors.
- Retrieval quality: run `make test` eval harness.

## Troubleshooting
- Empty citations: verify policy files in `data/sample_policies` and rerun ingestion.
- 429 errors: increase `RATE_LIMIT_PER_MINUTE`.
- Azure auth issues: keep `AUTH_MODE=mock` until Entra settings are configured.
