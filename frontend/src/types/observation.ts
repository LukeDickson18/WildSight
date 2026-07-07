export interface ObservationSpecies {
  id: string;
  common_name: string;
  scientific_name: string;
  ebird_code: string;
}

export interface ObservationLocation {
  id: string;
  name: string | null;
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

  location: ObservationLocation | null;

  user: ObservationUser;

  created_at: string;

  updated_at: string;
}

export interface ObservationListResponse {
  items: Observation[];

  total: number;

  page: number;

  page_size: number;

  total_pages: number;
}

export interface ObservationCreate {
  species_id: string;

  latitude: number;
  longitude: number;

  observation_datetime: string;

  count: number;

  notes?: string;
}

export interface ObservationUpdate {
  observation_datetime?: string;

  count?: number;

  notes?: string;
}

/**
 * Parameters used when requesting observations from the API.
 */
export interface ObservationQueryParams {
  page?: number;

  pageSize?: number;

  search?: string;

  speciesId?: string;

  startDate?: string;

  endDate?: string;

  sort?: ObservationSort;

  token?: string;
}

export type ObservationSort =
  | "newest"
  | "oldest"
  | "species"
  | "updated";