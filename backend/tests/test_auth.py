from collections.abc import Generator
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.session import get_db
from app.main import app
from app.models.user import User


@pytest.fixture()
def db() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.execute(delete(User).where(User.username.like("testuser_%")))
        session.commit()
        session.close()


@pytest.fixture()
def client(db: Session) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield db

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def register_payload(
    email: str | None = None,
    username: str | None = None,
    password: str = "correct-password",
) -> dict[str, str]:
    unique = uuid4().hex
    return {
        "email": email or f"testuser_{unique}@example.com",
        "username": username or f"testuser_{unique}",
        "password": password,
    }


def test_successful_registration(client: TestClient) -> None:
    response = client.post("/auth/register", json=register_payload())

    assert response.status_code == 201
    body = response.json()
    assert body["email"].startswith("testuser_")
    assert body["username"].startswith("testuser_")
    assert "hashed_password" not in body


def test_duplicate_email(client: TestClient) -> None:
    payload = register_payload()

    first_response = client.post("/auth/register", json=payload)
    second_response = client.post(
        "/auth/register",
        json=register_payload(email=payload["email"]),
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email is already registered"


def test_duplicate_username(client: TestClient) -> None:
    payload = register_payload()

    first_response = client.post("/auth/register", json=payload)
    second_response = client.post(
        "/auth/register",
        json=register_payload(username=payload["username"]),
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Username is already registered"


def test_invalid_login(client: TestClient) -> None:
    payload = register_payload(password="correct-password")
    client.post("/auth/register", json=payload)

    response = client.post(
        "/auth/login",
        json={
            "email": payload["email"],
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_successful_login(client: TestClient) -> None:
    payload = register_payload(password="correct-password")
    client.post("/auth/register", json=payload)

    response = client.post(
        "/auth/login",
        json={
            "email": payload["email"],
            "password": payload["password"],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["access_token"]
    assert body["token_type"] == "bearer"


def test_invalid_jwt(client: TestClient) -> None:
    response = client.get(
        "/me",
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 401


def test_authenticated_me_endpoint(client: TestClient) -> None:
    payload = register_payload(password="correct-password")
    client.post("/auth/register", json=payload)
    login_response = client.post(
        "/auth/login",
        json={
            "email": payload["email"],
            "password": payload["password"],
        },
    )

    token = login_response.json()["access_token"]
    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == payload["email"]
    assert body["username"] == payload["username"]
    assert "hashed_password" not in body
