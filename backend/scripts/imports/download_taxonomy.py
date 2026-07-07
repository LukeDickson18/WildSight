from pathlib import Path

from backend.app.enrichment.ebird import EBirdClient


def download_taxonomy():

    client = EBirdClient()

    output = Path("data/raw/ebird/taxonomy.csv")

    client.download_taxonomy(output)


if __name__ == "__main__":
    main()