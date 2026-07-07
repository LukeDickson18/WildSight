from backend.app.enrichment.ebird import EBirdClient


def test_get_taxonomy():
    client = EBirdClient()

    taxonomy = client.get_taxonomy()

    print(taxonomy[:1000])


if __name__ == "__main__":
    test_get_taxonomy()