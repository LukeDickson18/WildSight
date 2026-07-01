# Database Design

## Planned Tables

### Users

* id
* username
* email
* password_hash
* created_at

---

### Species

* id
* common_name
* scientific_name
* kingdom
* phylum
* class
* order
* family
* genus
* taxonomic_group
* conservation_status
* description

---

### Observations

* id
* user_id
* species_id
* latitude
* longitude
* observation_date
* confidence_score
* notes

---

### Images

* id
* observation_id
* image_url
* upload_date

---

### Locations

* id
* name
* country
* province
* latitude
* longitude

---

## Relationships

```
Users
    │
    └── Observations
            │
            ├── Images
            │
            ├── Species
            │
            └── Locations
```

The schema is intentionally designed to support every type of wildlife rather than only birds.
