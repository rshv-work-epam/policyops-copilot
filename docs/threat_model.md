# Threat Model (STRIDE)
- **Spoofing**: mock header auth only for local; Entra JWT required in cloud.
- **Tampering**: audit logs append-only pattern; DB role separation recommended.
- **Repudiation**: approvals and audit entries store actor + timestamps + correlation id.
- **Information Disclosure**: no secrets in code; Key Vault and env vars.
- **Denial of Service**: in-memory rate limit + Container Apps scale rules.
- **Elevation of Privilege**: admin routes enforce role checks.
