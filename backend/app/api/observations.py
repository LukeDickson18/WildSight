from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.repositories.observation_repository import ObservationRepository

from app.schemas.observations import (
    ObservationCreate,
    ObservationListResponse,
    ObservationResponse,
    ObservationUpdate,
)
from app.services.observation_service import ObservationService

router = APIRouter(
    prefix="/observations",
    tags=["Observations"],
)


from app.repositories.location_repository import LocationRepository

def get_observation_service(
    db: Session = Depends(get_db),
) -> ObservationService:

    observation_repository = ObservationRepository(db)
    location_repository = LocationRepository(db)

    return ObservationService(
        observation_repository,
        location_repository,
    )

@router.get(
    "",
    response_model=ObservationListResponse,
    summary="Get observations",
)
def get_observations(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: ObservationService = Depends(get_observation_service),
) -> ObservationListResponse:
    return service.get_observations(
        page=page,
        page_size=page_size,
    )


@router.get(
    "/{observation_id}",
    response_model=ObservationResponse,
    summary="Get observation by ID",
)
def get_observation(
    observation_id: UUID,
    service: ObservationService = Depends(get_observation_service),
) -> ObservationResponse:
    return service.get_observation_by_id(observation_id)


@router.post(
    "",
    response_model=ObservationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create observation",
)
def create_observation(
    observation: ObservationCreate,
    current_user: User = Depends(get_current_user),
    service: ObservationService = Depends(get_observation_service),
) -> ObservationResponse:
    return service.create_observation(
        data=observation,
        user_id=current_user.id,
    )


@router.put(
    "/{observation_id}",
    response_model=ObservationResponse,
    summary="Update observation",
)
def update_observation(
    observation_id: UUID,
    observation: ObservationUpdate,
    service: ObservationService = Depends(get_observation_service),
) -> ObservationResponse:
    return service.update_observation(
        observation_id=observation_id,
        data=observation,
    )


@router.delete(
    "/{observation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete observation",
)
def delete_observation(
    observation_id: UUID,
    service: ObservationService = Depends(get_observation_service),
) -> Response:
    service.delete_observation(observation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)