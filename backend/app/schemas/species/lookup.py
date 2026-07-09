from uuid import UUID

from pydantic import BaseModel


class CountryLookup(BaseModel):
    id: UUID
    name: str
    iso_code: str


class OrderLookup(BaseModel):
    id: UUID
    common_name: str
    scientific_name: str


class FamilyLookup(BaseModel):
    id: UUID
    common_name: str
    scientific_name: str


class HotspotLookup(BaseModel):
    id: UUID
    name: str