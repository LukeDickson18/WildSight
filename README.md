# WildSight

WildSight is a full-stack wildlife observation, analytics, and prediction platform. It enables users to record wildlife sightings, enrich observations with environmental data, and generate insights that help predict when and where species are most likely to be observed.

The project is designed with scalability in mind. Although the initial focus is on bird observations, the architecture is built to support all wildlife, including mammals, reptiles, amphibians, insects, marine life, and plants.

## Features (Planned)

* Record and manage wildlife observations
* Interactive maps and observation hotspots
* Environmental data enrichment (weather, season, habitat, etc.)
* Species analytics and reporting
* Machine learning prediction engine
* Community observation sharing

## Technology Stack

### Frontend

* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### Database

* PostgreSQL
* PostGIS

### Data Engineering

* Python ETL pipelines
* Feature engineering
* Scheduled data processing

### Machine Learning

* scikit-learn

### DevOps

* Docker
* Docker Compose
* GitHub Actions (planned)

---

## Getting Started

### Prerequisites

* Docker Desktop
* Git

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

To rebuild after dependency changes:

```bash
docker compose up --build
```

---

## Project Structure

```
WildSight/
├── backend/
├── frontend/
├── docs/
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Project Status

Active Development

WildSight is currently in the initial development phase. The current focus is establishing the project architecture, development environment, and core backend and frontend infrastructure.

---

## License

This project is licensed under the MIT License.
