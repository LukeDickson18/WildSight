from pathlib import Path
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class EBirdClient:
    """Client for interacting with the eBird API."""

    BASE_URL = "https://api.ebird.org/v2"

    def __init__(self):
        api_key = os.getenv("EBIRD_API_KEY")

        if not api_key:
            raise ValueError("EBIRD_API_KEY not found.")

        self.headers = {
            "X-eBirdApiToken": api_key,
        }

    def _get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        """
        Send a GET request to the eBird API.
        """

        response = requests.get(
            f"{self.BASE_URL}/{endpoint}",
            headers=self.headers,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response

    def get_taxonomy(self, fmt: str = "csv"):
        """
        Retrieve the complete eBird taxonomy.

        Parameters
        ----------
        fmt : str
            Response format ("csv" or "json").

        Returns
        -------
        str | list | dict
            Taxonomy in the requested format.
        """

        response = self._get(
            "ref/taxonomy/ebird",
            {"fmt": fmt},
        )

        return response.text if fmt == "csv" else response.json()

    def download_taxonomy(self, output_path: Path):
        """
        Download the taxonomy and save it locally.
        """

        taxonomy = self.get_taxonomy(fmt="csv")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        output_path.write_text(
            taxonomy,
            encoding="utf-8",
        )

        print(f"✓ Saved taxonomy to {output_path}")

    def get_species_codes(self, region_code: str) -> list[str]:
        """
        Return all eBird species codes recorded in a region.

        Parameters
        ----------
        region_code : str
            eBird region code (e.g. ZA, BW, NA).

        Returns
        -------
        list[str]
            List of eBird species codes.
        """

        response = self._get(
            f"product/spplist/{region_code}"
        )

        return response.json()
    
    def get_hotspots(
        self,
        region_code: str,
        fmt: str = "csv",
    ):
        """
        Retrieve all hotspots for an eBird region.

        Parameters
        ----------
        region_code : str
            eBird region code (e.g. ZA, ZA-WC).

        fmt : str
            Response format ("csv" or "json").

        Returns
        -------
        str | list
            Hotspot data.
        """

        response = self._get(
            f"ref/hotspot/{region_code}",
            {"fmt": fmt},
        )

        return response.text if fmt == "csv" else response.json()
    
    def download_hotspots(
        self,
        region_code: str,
        output_path: Path,
    ):
            """
            Download hotspot CSV for a region.
            """

            hotspots = self.get_hotspots(
                region_code=region_code,
                fmt="csv",
            )

            output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            output_path.write_text(
                hotspots,
                encoding="utf-8",
            )

            print(f"✓ Saved hotspots to {output_path}")