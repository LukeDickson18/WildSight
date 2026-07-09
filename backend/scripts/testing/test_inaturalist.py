from app.enrichment.inaturalist import INaturalistClient


TEST_SPECIES = [
    ("Cossypha caffra", "Cape Robin-Chat"),
    ("Ichthyophaga vocifer", "African Fish Eagle"),
    ("Numida meleagris", "Helmeted Guineafowl"),
    ("Phoenicopterus roseus", "Greater Flamingo"),
    ("Colius striatus", "Speckled Mousebird"),
]


def main() -> None:
    client = INaturalistClient()

    for scientific_name, common_name in TEST_SPECIES:

        print("-" * 80)
        print(f"Scientific Name : {scientific_name}")
        print(f"Common Name     : {common_name}")

        image = client.get_species_photo(
            scientific_name=scientific_name,
            common_name=common_name,
        )

        if image is None:
            print("❌ No image found.")
            continue

        print(f"iNat Taxon ID : {image['inat_taxon_id']}")
        print(f"Image URL     : {image['image_url']}")
        print(f"Thumbnail     : {image['thumbnail_url']}")
        print(f"License       : {image['image_license']}")
        print(f"Attribution   : {image['image_attribution']}")
        print(f"Source        : {image['image_source']}")

    print("-" * 80)
    print("Finished.")


if __name__ == "__main__":
    main()