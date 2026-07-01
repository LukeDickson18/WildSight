# System Architecture

## Overview

The application follows a modular client-server architecture that separates the mobile application, backend services, machine learning pipeline, and database.

```
             iOS Application
                    │
                    ▼
              REST API Gateway
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
 Authentication Service     Wildlife Service
      │                           │
      └─────────────┬─────────────┘
                    ▼
               PostgreSQL
                    │
                    ▼
         Machine Learning Service
```

---

## Components

### iOS Application

Responsibilities:

* User authentication
* Camera integration
* Image upload
* Viewing observations
* Wildlife search
* Maps
* Personal collections

---

### Backend API

Responsibilities:

* Authentication
* User management
* Species retrieval
* Observation management
* Image processing
* Communication with machine learning services

---

### Database

Stores:

* Users
* Species
* Observations
* Images
* Locations
* Statistics

---

### Machine Learning

Responsibilities:

* Species identification
* Confidence estimation
* Model inference
* Future model training

---

## Design Principles

* Modular
* Scalable
* Cloud-ready
* Easy to maintain
* Independent services where appropriate
