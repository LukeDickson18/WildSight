from app.services.ebird import EBirdClient


def main():
    client = EBirdClient()

    taxonomy = client.get_taxonomy()

    print(taxonomy[:1000])


if __name__ == "__main__":
    main()