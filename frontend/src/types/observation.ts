export interface ObservationSpecies {
    id: string;
    common_name: string;
    scientific_name: string;
    ebird_code: string;
}

export interface ObservationLocation {
    id: string;
    name: string;
}

export interface ObservationUser {
    id: string;
    username: string;
}

export interface Observation {
    id: string;

    observation_datetime: string;

    count: number;

    notes: string | null;

    species: ObservationSpecies;

    location: ObservationLocation;

    user: ObservationUser;

    created_at: string;

    updated_at: string;
}

export interface ObservationListResponse {
    items: Observation[];
    total: number;
    page: number;
    page_size: number;
}

export type ObservationCreate = {
  species_id: string;

  latitude: number;
  longitude: number;

  observation_datetime: string;

  count: number;

  notes: string | null;
};

export interface ObservationUpdate {
    species_id?: string;

    location_id?: string;

    observation_datetime?: string;

    count?: number;

    notes?: string;
}