export interface SpeciesFilterState {
  search: string;
  useMyLocation: boolean;
  
  latitude?: number;
  longitude?: number;

  radius: string;


  countryId: string;
  orderId: string;
  familyId: string;
  hotspotId: string;
}

export const defaultSpeciesFilters: SpeciesFilterState = {
  search: "",

  useMyLocation: false,
  radius: "50",

  countryId: "",
  orderId: "",
  familyId: "",
  hotspotId: "",
};

/**
 * Filters sent to the backend Species Explorer API.
 */
export interface SpeciesExplorerFilters {
  search?: string;

  orderId?: string;
  familyId?: string;
  countryId?: string;

  latitude?: number;
  longitude?: number;
  radiusKm?: number;

  hotspotId?: string;

  page?: number;
  pageSize?: number;
}