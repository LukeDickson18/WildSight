# API Design

## Authentication

POST /register

POST /login

POST /logout

GET /profile

---

## Species

GET /species

GET /species/{id}

GET /species/search

---

## Observations

GET /observations

POST /observations

PUT /observations/{id}

DELETE /observations/{id}

---

## Identification

POST /identify

Input

* Wildlife image

Output

* Predicted species
* Confidence score
* Top predictions

---

## User

GET /user

PUT /user

GET /user/lifelist

---

## Future Endpoints

* Community observations
* Leaderboards
* Wildlife hotspots
* Species distribution maps
* Prediction service
