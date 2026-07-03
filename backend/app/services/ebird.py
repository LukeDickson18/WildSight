from pathlib import Path
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

    def download_taxonomy(self, output_path: Path):

        taxonomy = self.get_taxonomy(fmt="csv")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        output_path.write_text(taxonomy, encoding="utf-8")

        print(f"✓ Saved taxonomy to {output_path}")