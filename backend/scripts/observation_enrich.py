from app.db.database import SessionLocal
from app.services.observation_enrichment_service import (
    ObservationEnrichmentService,
)


def main():

    db = SessionLocal()

    try:
        service = ObservationEnrichmentService(db)

        enriched = service.enrich_all()

        print(f"Successfully enriched {enriched} observations.")

    finally:
        db.close()


if __name__ == "__main__":
    main()