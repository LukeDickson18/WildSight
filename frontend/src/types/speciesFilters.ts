export interface SpeciesFilterState {
    search: string;

    useMyLocation: boolean;
    radius: string;

    country: string;
    hotspot: string;
}

export const defaultSpeciesFilters: SpeciesFilterState = {
    search: "",
    useMyLocation: false,
    radius: "50",
    country: "South Africa",
    hotspot: "Any",
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