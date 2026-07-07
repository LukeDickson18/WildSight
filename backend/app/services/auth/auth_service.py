from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth.jwt import create_access_token
from app.auth.password import hash_password, verify_password
from app.models.user import User
from app.schemas.auth.auth import LoginRequest, RegisterRequest, TokenResponse


def get_user_by_id(db: Session, user_id: UUID) -> User | None:
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email.lower())
    return db.execute(statement).scalar_one_or_none()


def get_user_by_username(db: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return db.execute(statement).scalar_one_or_none()


def register_user(db: Session, request: RegisterRequest) -> User:
    email = request.email.lower()

    if get_user_by_email(db, email) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )

    if get_user_by_username(db, request.username) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username is already registered",
        )

    user = User(
        email=email,
        username=request.username,
        hashed_password=hash_password(request.password),
    )
    db.add(user)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        ) from exc

    db.refresh(user)
    return user


def authenticate_user(db: Session, request: LoginRequest) -> User | None:
    user = get_user_by_email(db, request.email)
    if user is None:
        return None

    if not verify_password(request.password, user.hashed_password):
        return None

    return user


def login_user(db: Session, request: LoginRequest) -> TokenResponse:
    user = authenticate_user(db, request)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(subject=str(user.id))
    return TokenResponse(access_token=access_token)
