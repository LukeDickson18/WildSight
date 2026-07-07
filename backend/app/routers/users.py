from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.observation import Observation
from app.models.user import User
from app.schemas.observation import ObservationRead
from app.schemas.user import UserRead, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserRead,
)
def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.patch(
    "/me",
    response_model=UserRead,
)
def update_current_user(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(current_user, field, value)

    db.commit()
    db.refresh(current_user)

    return current_user


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.get(
    "/{user_id}/observations",
    response_model=list[ObservationRead],
)
def get_user_observations(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    observations = db.scalars(
        select(Observation).where(
            Observation.user_id == user_id
        )
    ).all()

    return observations


@router.delete(
    "/me",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_current_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db.delete(current_user)
    db.commit()