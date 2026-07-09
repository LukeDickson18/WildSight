import { request } from "./client";

import type {
    Species,
    SpeciesExplorerResponse,
    SpeciesListResponse,
} from "../types/species";

import type {
    SpeciesExplorerFilters,
} from "../types/speciesFilters";

export async function getSpeciesExplorer(
    filters: SpeciesExplorerFilters = {},
): Promise<SpeciesExplorerResponse> {
    const params = new URLSearchParams();

    if (filters.search) {
        params.set("search", filters.search);
    }

    if (filters.orderId) {
        params.set("order_id", filters.orderId);
    }

    if (filters.familyId) {
        params.set("family_id", filters.familyId);
    }

    if (filters.countryId) {
        params.set("country_id", filters.countryId);
    }

    if (
        filters.latitude !== undefined &&
        filters.longitude !== undefined
    ) {
        params.set("latitude", filters.latitude.toString());
        params.set("longitude", filters.longitude.toString());
    }

    if (filters.radiusKm !== undefined) {
        params.set("radius_km", filters.radiusKm.toString());
    }

    if (filters.hotspotId) {
        params.set("hotspot_id", filters.hotspotId);
    }

    params.set("page", (filters.page ?? 1).toString());
    params.set("page_size", (filters.pageSize ?? 25).toString());

    return request(`/species/explorer?${params.toString()}`);
}

export async function searchSpecies(
    query: string,
    page = 1,
    pageSize = 10,
): Promise<SpeciesListResponse> {
    const params = new URLSearchParams();

    params.set("search", query);
    params.set("page", page.toString());
    params.set("page_size", pageSize.toString());

    return request(`/species/explorer?${params.toString()}`);
}

export function getSpeciesById(
    id: string,
): Promise<Species> {
    return request(`/species/${id}`);
}