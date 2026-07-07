from app.db.database import SessionLocal
from backend.app.enrichment.observation import (
    ObservationEnrichmentService,
)


def enrich_observations():

    db = SessionLocal()

    try:
        service = ObservationEnrichmentService(db)

        enriched = service.enrich_all()

        print(f"Successfully enriched {enriched} observations.")

    finally:
        db.close()


if __name__ == "__main__":
    main()