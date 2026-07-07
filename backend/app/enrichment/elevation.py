from __future__ import annotations

from typing import Optional

import requests


class ElevationService:
    BASE_URL = "https://api.open-meteo.com/v1/elevation"

    @classmethod
    def get_elevation(cls, latitude: float, longitude: float) -> Optional[float]:
        try:
            response = requests.get(
                cls.BASE_URL,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                },
                timeout=15,
            )

            response.raise_for_status()

            data = response.json()

            elevations = data.get("elevation")

            if not elevations:
                return None

            return float(elevations[0])

        except Exception:
            return None