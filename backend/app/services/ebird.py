import os

import requests
from dotenv import load_dotenv

load_dotenv()


class EBirdClient:
    BASE_URL = "https://api.ebird.org/v2"

    def __init__(self):
        api_key = os.getenv("EBIRD_API_KEY")

        if not api_key:
            raise ValueError("EBIRD_API_KEY not found.")

        self.headers = {
            "X-eBirdApiToken": api_key
        }

    def get_taxonomy(self, fmt: str = "csv"):

        url = f"{self.BASE_URL}/ref/taxonomy/ebird"

        response = requests.get(
            url,
            headers=self.headers,
            params={"fmt": fmt},
            timeout=30,
        )

        response.raise_for_status()

        return response.text if fmt == "csv" else response.json()