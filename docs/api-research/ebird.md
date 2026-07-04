# eBird API Research

## Overview

eBird is the primary external biodiversity data source for WildSight.

It provides:

- Bird taxonomy
- Species codes
- Scientific names
- Recent observations
- Hotspots
- Regional species lists
- Checklists

WildSight does **not** depend on eBird for storing user observations.

Instead, eBird is used to enrich the application with authoritative bird data.

---

## Authentication

Authentication:
API Key

Header:

x-ebirdapitoken: <API_KEY>

The API key is stored as an environment variable on the backend.

Frontend clients never communicate directly with eBird.

---

## Data Ownership

WildSight owns:

- Users
- Observations
- Photos
- Locations
- Weather snapshots

eBird owns:

- Taxonomy
- Hotspots
- Regional bird lists
- Recent public observations