from sqlalchemy import select

from app.db.database import SessionLocal
from app.models.species_display_group import SpeciesDisplayGroup

GROUPS = [
    "Pelagics",
    "Birds of Prey",
    "Waterfowl",
    "Gamebirds",
    "Shorebirds",
    "Herons & Egrets",
    "Storks",
    "Flamingos",
    "Gulls & Terns",
    "Pigeons & Doves",
    "Owls",
    "Kingfishers",
    "Bee-eaters",
    "Rollers",
    "Hornbills",
    "Woodpeckers",
    "Parrots",
    "Cuckoos",
    "Swifts",
    "Swallows",
    "Larks",
    "Pipits & Wagtails",
    "Warblers & Cisticolas",
    "Flycatchers",
    "Chats",
    "Thrushes",
    "Starlings",
    "Weavers",
    "Waxbills",
    "Sunbirds",
    "Shrikes",
    "Crows & Ravens",
    "Other Birds",
]


def main() -> None:
    db = SessionLocal()

    try:
        for order, name in enumerate(GROUPS, start=1):
            exists = db.scalar(
                select(SpeciesDisplayGroup).where(
                    SpeciesDisplayGroup.name == name
                )
            )

            if exists:
                continue

            db.add(
                SpeciesDisplayGroup(
                    name=name,
                    wildlife_group="Bird",
                    display_order=order,
                )
            )

        db.commit()

        print(f"Seeded {len(GROUPS)} display groups.")

    finally:
        db.close()


if __name__ == "__main__":
    main()