from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="WildSight")


def reverse_geocode(
    latitude: float,
    longitude: float,
) -> dict:

    try:
        result = geocoder.reverse(
            (latitude, longitude),
            language="en",
            exactly_one=True,
        )

        if result is None:
            return {}

        address = result.raw.get("address", {})

        return {
            "country": address.get("country"),
            "state_province": (
                address.get("state")
                or address.get("province")
            ),
            "municipality": (
                address.get("city")
                or address.get("town")
                or address.get("municipality")
                or address.get("county")
            ),
            "locality": (
                address.get("suburb")
                or address.get("village")
                or address.get("hamlet")
                or address.get("neighbourhood")
            ),
        }

    except (
        GeocoderTimedOut,
        GeocoderUnavailable,
    ):
        return {}