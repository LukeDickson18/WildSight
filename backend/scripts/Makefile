.PHONY: \
	help \
	migrate \
	db-reset \
	dev-setup \
	rebuild \
	taxonomy taxonomy-download taxonomy-transform taxonomy-load \
	hotspots hotspots-download hotspots-load \
	countries distribution \
	seed \
	enrich enrich-location enrich-weather enrich-astronomy enrich-elevation enrich-hotspots

# ==========================================================
# Help
# ==========================================================

help:
	@echo ""
	@echo "WildSight Development Commands"
	@echo "=============================="
	@echo ""
	@echo "Database"
	@echo "  make migrate        Apply Alembic migrations"
	@echo "  make db-reset       Apply migrations to a fresh database"
	@echo "  make rebuild        Rebuild containers and recreate development database"
	@echo "  make dev-setup      Complete development setup"
	@echo ""
	@echo "Data"
	@echo "  make taxonomy"
	@echo "  make hotspots"
	@echo "  make countries"
	@echo "  make distribution"
	@echo ""
	@echo "Seeding"
	@echo "  make seed"
	@echo ""
	@echo "Enrichment"
	@echo "  make enrich"
	@echo ""

# ==========================================================
# Database
# ==========================================================

migrate:
	docker compose exec backend alembic upgrade head

db-reset: migrate

rebuild:
	docker compose up -d
	@echo "Waiting for PostgreSQL..."
	@sleep 10
	$(MAKE) dev-setup

dev-setup: db-reset countries taxonomy distribution hotspots seed enrich
	@echo ""
	@echo "=========================================="
	@echo " WildSight development environment ready"
	@echo "=========================================="

# ==========================================================
# Taxonomy
# ==========================================================

taxonomy-download:
	docker compose exec backend python -m scripts.data.download_taxonomy

taxonomy-transform:
	docker compose exec backend python -m scripts.data.transform_raw_ebird

taxonomy-load:
	docker compose exec backend python -m scripts.data.load_taxonomy

taxonomy:
	$(MAKE) taxonomy-download
	$(MAKE) taxonomy-transform
	$(MAKE) taxonomy-load

# ==========================================================
# Hotspots
# ==========================================================

hotspots-download:
	docker compose exec backend python -m scripts.data.download_hotspots

hotspots-load:
	docker compose exec backend python -m scripts.data.load_hotspots

hotspots:
	$(MAKE) hotspots-download
	$(MAKE) hotspots-load

# ==========================================================
# Countries & Distribution
# ==========================================================

countries:
	docker compose exec backend python -m scripts.data.seed_countries

distribution:
	docker compose exec backend python -m scripts.data.load_species_distribution

# ==========================================================
# Development Seeding
# ==========================================================

seed:
	docker compose exec backend python -m scripts.seeding.development

# ==========================================================
# Enrichment
# ==========================================================

enrich-location:
	docker compose exec backend python -m scripts.enrichment.location

enrich-weather:
	docker compose exec backend python -m scripts.enrichment.weather

enrich-astronomy:
	docker compose exec backend python -m scripts.enrichment.astronomy

enrich-elevation:
	docker compose exec backend python -m scripts.enrichment.elevation

enrich-hotspots:
	docker compose exec backend python -m scripts.enrichment.hotspot

enrich-images:
	docker compose exec backend python -m scripts.enrichment.species_images
enrich:
	$(MAKE) enrich-location
	$(MAKE) enrich-elevation
	$(MAKE) enrich-weather
	$(MAKE) enrich-astronomy
	$(MAKE) enrich-hotspots
	$(MAKE) enrich-images