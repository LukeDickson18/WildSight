from datetime import date

from astral import LocationInfo
from astral.moon import phase
from astral.sun import sun
from zoneinfo import ZoneInfo


TIMEZONE = "Africa/Johannesburg"


def get_season(month: int) -> str:
    if month in (12, 1, 2):
        return "Summer"
    elif month in (3, 4, 5):
        return "Autumn"
    elif month in (6, 7, 8):
        return "Winter"
    return "Spring"


def get_moon_phase_name(value: float) -> str:
    if value < 1.75:
        return "New Moon"
    elif value < 5.25:
        return "Waxing Crescent"
    elif value < 8.75:
        return "First Quarter"
    elif value < 12.25:
        return "Waxing Gibbous"
    elif value < 15.75:
        return "Full Moon"
    elif value < 19.25:
        return "Waning Gibbous"
    elif value < 22.75:
        return "Last Quarter"
    elif value < 26.25:
        return "Waning Crescent"
    return "New Moon"


def get_astronomy(
    latitude: float,
    longitude: float,
    observation_date: date,
) -> dict:

    location = LocationInfo(
        latitude=latitude,
        longitude=longitude,
        timezone=TIMEZONE,
    )

    s = sun(
        location.observer,
        date=observation_date,
        tzinfo=ZoneInfo(TIMEZONE),
    )

    daylight = (
        s["sunset"] - s["sunrise"]
    ).total_seconds() / 3600

    moon = phase(observation_date)

    return {
        "sunrise": s["sunrise"],
        "sunset": s["sunset"],
        "day_length": round(daylight, 2),
        "season": get_season(observation_date.month),
        "moon_phase": get_moon_phase_name(moon),
        "moon_illumination": round((moon / 29.53) * 100, 1),
    }