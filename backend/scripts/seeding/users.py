from app.db.database import SessionLocal
from app.models.user import User
from app.auth.password import hash_password

from sqlalchemy import select


DEMO_USERS = [
    {
        "username": "luked",
        "email": "luke@example.com",
        "password": "Password123!",
        "is_superuser": True,
    },
    {
        "username": "birder1",
        "email": "birder1@example.com",
        "password": "Password123!",
        "is_superuser": False,
    },
    {
        "username": "birder2",
        "email": "birder2@example.com",
        "password": "Password123!",
        "is_superuser": False,
    },
]


def seed_users() -> None:
    db = SessionLocal()

    try:
        created = 0
        skipped = 0

        for user_data in DEMO_USERS:
            existing = db.scalar(
                select(User).where(
                    User.email == user_data["email"]
                )
            )

            if existing:
                skipped += 1
                continue

            user = User(
                username=user_data["username"],
                email=user_data["email"],
                hashed_password=hash_password(user_data["password"]),
                is_superuser=user_data["is_superuser"],
            )

            db.add(user)
            created += 1

        db.commit()

        print(f"Created : {created}")
        print(f"Skipped : {skipped}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()