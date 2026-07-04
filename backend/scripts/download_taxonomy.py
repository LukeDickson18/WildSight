from pathlib import Path

from app.services.ebird import EBirdClient


def main():

    client = EBirdClient()

    output = Path("data/raw/ebird/taxonomy.csv")

    client.download_taxonomy(output)


if __name__ == "__main__":
    main()