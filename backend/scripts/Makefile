.PHONY: taxonomy hotspots countries distribution enrich seed

# -------------------------
# Taxonomy
# -------------------------

taxonomy-download:
	docker compose exec backend python -m scripts.data.download_taxonomy

taxonomy-transform:
	docker compose exec backend python -m scripts.data.transform_taxonomy

taxonomy-load:
	docker compose exec backend python -m scripts.data.load_taxonomy

taxonomy:
	docker compose exec backend python -m scripts.data.download_taxonomy
	docker compose exec backend python -m scripts.data.transform_taxonomy
	docker compose exec backend python -m scripts.data.load_taxonomy

# -------------------------
# Hotspots
# -------------------------

hotspots-download:
	docker compose exec backend python -m scripts.data.download_hotspots

hotspots-load:
	docker compose exec backend python -m scripts.data.load_hotspots

hotspots:
	docker compose exec backend python -m scripts.data.download_hotspots
	docker compose exec backend python -m scripts.data.load_hotspots

# -------------------------
# Countries
# -------------------------

countries:
	docker compose exec backend python -m scripts.data.seed_countries

distribution:
	docker compose exec backend python -m scripts.data.load_species_distribution

# -------------------------
# Enrichment
# -------------------------

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

enrich:
	docker compose exec backend python -m scripts.enrichment.location
	docker compose exec backend python -m scripts.enrichment.elevation
	docker compose exec backend python -m scripts.enrichment.weather
	docker compose exec backend python -m scripts.enrichment.astronomy
	docker compose exec backend python -m scripts.enrichment.hotspot