from uuid import UUID

from fastapi import HTTPException, status

from app.repositories.hotspots import HotspotRepository
from app.schemas.hotspots import (
    HotspotListResponse,
    HotspotResponse,
    NearbyHotspotListResponse,
    NearbyHotspotResponse,
)


class HotspotService:
    def __init__(
        self,
        repository: HotspotRepository,
    ):
        self.repository = repository

    def get_hotspots(
        self,
        page: int,
        page_size: int,
    ) -> HotspotListResponse:

        hotspots, total = self.repository.get_hotspots(
            page=page,
            page_size=page_size,
        )

        return HotspotListResponse(
            items=hotspots,
            total=total,
            page=page,
            page_size=page_size,
        )

    def get_hotspot_by_id(
        self,
        hotspot_id: UUID,
    ) -> HotspotResponse:

        hotspot = self.repository.get_hotspot_by_id(
            hotspot_id
        )

        if hotspot is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hotspot not found.",
            )

        return hotspot

    def get_nearby_hotspots(
        self,
        latitude: float,
        longitude: float,
        radius: int,
        page: int,
        page_size: int,
    ) -> NearbyHotspotListResponse:

        rows, total = self.repository.get_nearby_hotspots(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            page=page,
            page_size=page_size,
        )

        hotspots = [
            NearbyHotspotResponse(
                id=hotspot.id,
                ebird_id=hotspot.ebird_id,
                name=hotspot.name,
                source=hotspot.source,
                latitude=hotspot.latitude,
                longitude=hotspot.longitude,
                distance_km=round(distance_km, 2),
            )
            for hotspot, distance_km in rows
        ]

        return NearbyHotspotListResponse(
            items=hotspots,
            total=total,
            page=page,
            page_size=page_size,
        )