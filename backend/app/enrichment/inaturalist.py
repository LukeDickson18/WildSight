from __future__ import annotations

import time

import requests

BASE_URL = "https://api.inaturalist.org/v1"

# Licenses that are safe to display with attribution.
ALLOWED_LICENSES = {
    "cc0",
    "cc-by",
    "cc-by-sa",
    "cc-by-nd",
    "cc-by-nc",
    "cc-by-nc-sa",
    "cc-by-nc-nd",
}


class INaturalistClient:
    def __init__(
        self,
        timeout: int = 20,
        max_retries: int = 3,
    ) -> None:
        self.timeout = timeout
        self.max_retries = max_retries

        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "WildSight/1.0",
                "Accept": "application/json",
            }
        )

    def _request(
        self,
        params: dict,
    ) -> list[dict]:

        for attempt in range(self.max_retries):
            try:
                response = self.session.get(
                    f"{BASE_URL}/taxa",
                    params=params,
                    timeout=self.timeout,
                )

                response.raise_for_status()

                return response.json().get("results", [])

            except requests.RequestException:

                if attempt == self.max_retries - 1:
                    return []

                time.sleep(2**attempt)

        return []

    def _find_taxon(
        self,
        query: str,
        expected_scientific_name: str,
    ) -> dict | None:
        """
        Search iNaturalist and return the exact matching species.
        """

        results = self._request(
            {
                "q": query,
                "rank": "species",
                "per_page": 30,
            }
        )

        expected = expected_scientific_name.strip().lower()

        # Prefer an exact scientific-name match.
        for taxon in results:
            name = (taxon.get("name") or "").strip().lower()

            if name == expected:
                return taxon

        # Otherwise return the first species result.
        for taxon in results:
            if taxon.get("rank") == "species":
                return taxon

        return None

    def get_species_photo(
        self,
        scientific_name: str,
        common_name: str,
    ) -> dict | None:
        """
        Returns image metadata for a species.

        Searches by scientific name first and falls back to the
        common name if necessary.

        Only Creative Commons licensed photos are accepted.
        """

        taxon = self._find_taxon(
            scientific_name,
            scientific_name,
        )

        if taxon is None:
            taxon = self._find_taxon(
                common_name,
                scientific_name,
            )

        if taxon is None:
            return None

        photo = taxon.get("default_photo")

        if photo is None:
            return None

        license_code = photo.get("license_code")

        # Skip "All Rights Reserved" images.
        if (
            license_code is None
            or license_code.lower() not in ALLOWED_LICENSES
        ):
            return None

        thumbnail_url = (
            photo.get("medium_url")
            or photo.get("url")
        )

        image_url = photo.get("original_url")

        if image_url is None and thumbnail_url:
            image_url = (
                thumbnail_url
                .replace("/medium.", "/original.")
                .replace("medium.jpg", "original.jpg")
                .replace("medium.jpeg", "original.jpeg")
            )

        return {
            "inat_taxon_id": taxon.get("id"),
            "image_url": image_url,
            "thumbnail_url": thumbnail_url,
            "image_license": license_code,
            "image_attribution": photo.get("attribution"),
            "image_source": "iNaturalist",
        }