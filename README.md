# WildSight

## Project Overview

WildSight is a full-stack wildlife observation, analytics, and prediction platform designed to help users record, explore, and understand wildlife sightings.

The project begins with bird observations but is architected to support all wildlife, including mammals, reptiles, amphibians, insects, marine life, and plants. Each observation will eventually be enriched with environmental data such as weather, habitat, season, and location to provide deeper insights and power machine learning models that predict the likelihood of observing particular species under specific conditions.

WildSight is being developed as a production-quality software engineering portfolio project with an emphasis on scalable architecture, maintainable code, clean design, and modern development practices.

---

## Features

### Current
- Dockerized development environment
- FastAPI backend
- React frontend
- PostgreSQL database
- Modular project structure

### Planned
- Wildlife observation logging
- User authentication
- Interactive maps
- Observation hotspots
- Environmental data enrichment
- Species analytics dashboard
- Machine learning sighting predictions
- Community observation sharing

---

## Tech Stack

### Frontend
- React
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- Python

### Database
- PostgreSQL
- PostGIS

### Data Engineering
- Python
- ETL Pipelines
- Feature Engineering

### Machine Learning
- scikit-learn

### DevOps
- Docker
- Docker Compose
- GitHub Actions (planned)

---

## Architecture

WildSight follows a modular full-stack architecture.

```text
                +------------------+
                |      React       |
                |    Frontend      |
                +---------+--------+
                          |
                     REST API
                          |
                +---------v--------+
                |     FastAPI      |
                |     Backend      |
                +---------+--------+
                          |
                  SQLAlchemy ORM
                          |
                +---------v--------+
                |   PostgreSQL     |
                |    + PostGIS     |
                +------------------+
```

As the project evolves, additional services for environmental data ingestion, analytics, and machine learning will integrate with the backend.

---

## Setup Instructions

### Prerequisites

- Git
- Docker Desktop

### Clone the Repository

```bash
git clone https://github.com/LukeDickson18/WildSight.git
cd WildSight
```

### Build the Containers

```bash
docker compose build
```

### Start the Application

```bash
docker compose up
```

### Stop the Application

```bash
docker compose down
```

### Rebuild After Dependency Changes

```bash
docker compose up --build
```
### If out of sync
```bash
docker compose down --rmi local
```

### Complete refresh
```bash
docker compose down -v --rmi local
```
---

## Folder Structure

```text
WildSight/
│
├── backend/              # FastAPI application
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/             # React application
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docs/                 # Project documentation
│
├── docker-compose.yml
├── .gitignore
├── README.md
│
└── .env.example
```

---

## Roadmap

### Phase 1 — Foundation
- [x] Repository setup
- [x] Docker development environment
- [x] Backend and frontend scaffolding
- [ ] Database integration
- [ ] Initial API endpoints

### Phase 2 — Observation Platform
- [ ] Observation management
- [ ] Species database
- [ ] User authentication

### Phase 3 — Mapping & Analytics
- [ ] Interactive maps
- [ ] Observation hotspots
- [ ] Statistics dashboard

### Phase 4 — Environmental Data
- [ ] Weather integration
- [ ] Habitat enrichment
- [ ] Seasonal analysis

### Phase 5 — Machine Learning
- [ ] Feature engineering pipeline
- [ ] Prediction models
- [ ] Sighting probability forecasts

### Phase 6 — Community
- [ ] Shared observations
- [ ] User profiles
- [ ] Leaderboards
- [ ] Collaboration features

### Seeding 
docker compose exec backend python -m scripts.seeding.development 
### Enrich
docker compose exec backend python -m scripts.enrichment.location
docker compose exec backend python -m scripts.enrichment.elevation
docker compose exec backend python -m scripts.enrichment.weather
docker compose exec backend python -m scripts.enrichment.astronomy
docker compose exec backend python -m scripts.enrichment.hotspot