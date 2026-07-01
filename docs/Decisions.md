# Architecture Decisions

## Decision Log

### 2026-07-01

#### Overall Project Direction

The application will be designed as a wildlife platform rather than a bird-only application.

Bird identification will be the first supported feature, but every architectural decision should support future expansion to all wildlife categories.

---

#### Technology Stack

Frontend

* SwiftUI

Backend

* FastAPI (Python)

Database

* PostgreSQL

Machine Learning

* PyTorch

Version Control

* Git & GitHub

---

#### Design Principles

* Keep components modular
* Design database for all wildlife
* Expose functionality through REST APIs
* Keep machine learning independent of the mobile application

Future architectural decisions should be recorded below.
