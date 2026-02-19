from fastapi import Header, HTTPException

from app.core.config import settings


class Identity:
    def __init__(self, user_id: str, role: str) -> None:
        self.user_id = user_id
        self.role = role


def get_identity(x_mock_user: str | None = Header(default=None), x_mock_role: str | None = Header(default=None)) -> Identity:
    if settings.auth_mode == "mock":
        return Identity(x_mock_user or settings.mock_default_user, x_mock_role or settings.mock_default_role)
    raise HTTPException(status_code=501, detail="Entra ID mode not enabled in MVP runtime")
