from pathlib import Path

from app.enrichment.ebird import EBirdClient


def main():

    client = EBirdClient()

    client.download_hotspots(
        region_code="ZA",
        output_path=Path(
            "data/raw/ebird/hotspots.csv"
        ),
    )


if __name__ == "__main__":
    main()