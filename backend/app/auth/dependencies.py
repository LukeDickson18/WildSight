from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.auth.jwt import verify_access_token
from app.db.session import get_db
from app.models.user import User
from backend.app.services.auth.auth_service import get_user_by_id


bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(bearer_scheme),
    ],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None:
        raise credentials_exception

    payload = verify_access_token(credentials.credentials)
    if payload is None:
        raise credentials_exception

    subject = payload.get("sub")
    if not isinstance(subject, str):
        raise credentials_exception

    try:
        user_id = UUID(subject)
    except ValueError as exc:
        raise credentials_exception from exc

    user = get_user_by_id(db, user_id)
    if user is None or not user.is_active:
        raise credentials_exception

    return user
