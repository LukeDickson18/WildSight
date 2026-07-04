from pathlib import Path

import pandas as pd

# -----------------------------
# File Paths
# -----------------------------

RAW_TAXONOMY = Path("data/raw/ebird/taxonomy.csv")
PROCESSED_DIR = Path("data/processed/ebird")
OUTPUT_FILE = PROCESSED_DIR / "species.csv"

# -----------------------------
# Columns to Keep
# -----------------------------

COLUMNS = [
    "SCIENTIFIC_NAME",
    "COMMON_NAME",
    "SPECIES_CODE",
    "CATEGORY",
    "TAXON_ORDER",
    "ORDER",
    "FAMILY_COM_NAME",
    "FAMILY_SCI_NAME",
    "FAMILY_CODE",
]

# -----------------------------
# Rename Columns
# -----------------------------

COLUMN_MAPPING = {
    "SCIENTIFIC_NAME": "scientific_name",
    "COMMON_NAME": "common_name",
    "SPECIES_CODE": "ebird_code",
    "CATEGORY": "category",
    "TAXON_ORDER": "taxon_order",
    "ORDER": "order_name",
    "FAMILY_COM_NAME": "family_common_name",
    "FAMILY_SCI_NAME": "family_scientific_name",
    "FAMILY_CODE": "family_code",
}

# -----------------------------
# Required Fields
# -----------------------------

REQUIRED_COLUMNS = [
    "ebird_code",
    "common_name",
    "scientific_name",
    "category",
    "taxon_order",
    "order_name",
    "family_common_name",
    "family_scientific_name",
    "family_code",
]


def main() -> None:

    print("Loading eBird taxonomy...")

    taxonomy_df = pd.read_csv(RAW_TAXONOMY)

    print(f"Loaded {len(taxonomy_df):,} taxonomy records.")

    # Keep only species records
    species_df = taxonomy_df[
        taxonomy_df["CATEGORY"] == "species"
    ][COLUMNS]

    # Reset the index after filtering
    species_df = species_df.reset_index(drop=True)

    # Rename columns to match the database schema
    species_df = species_df.rename(columns=COLUMN_MAPPING)

    # Validate duplicate eBird codes
    duplicate_count = species_df["ebird_code"].duplicated().sum()

    if duplicate_count:
        raise ValueError(
            f"Found {duplicate_count} duplicate eBird species codes."
        )

    # Validate required columns
    for column in REQUIRED_COLUMNS:

        missing_count = species_df[column].isnull().sum()

        if missing_count > 0:
            raise ValueError(
                f"Column '{column}' contains {missing_count} missing values."
            )

    # Ensure output directory exists
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Save processed taxonomy
    species_df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print("\nTransformation Complete")
    print("-" * 50)
    print(f"Total taxonomy records : {len(taxonomy_df):,}")
    print(f"Species records        : {len(species_df):,}")
    print(f"Columns retained       : {len(species_df.columns)}")
    print(f"Output file            : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()