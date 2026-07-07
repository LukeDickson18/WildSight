from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from backend.app.schemas.auth.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from backend.app.services.auth.auth_service import login_user, register_user


router = APIRouter(tags=["Authentication"])


@router.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Annotated[Session, Depends(get_db)],
) -> User:
    return register_user(db, request)


@router.post("/auth/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Annotated[Session, Depends(get_db)],
) -> TokenResponse:
    return login_user(db, request)


@router.get("/me", response_model=UserResponse)
def read_me(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    return current_user
