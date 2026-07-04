import { request } from "./client";
import type { Species, SpeciesListResponse } from "../types/species";

export function getSpecies(
    page = 1,
    pageSize = 50,
): Promise<SpeciesListResponse> {
    return request(
        `/species?page=${page}&page_size=${pageSize}`
    );
}

export function searchSpecies(
    query: string,
    page = 1,
    pageSize = 50,
): Promise<SpeciesListResponse> {
    return request(
        `/species/search?q=${encodeURIComponent(query)}&page=${page}&page_size=${pageSize}`
    );
}

export function getSpeciesById(
    id: string,
): Promise<Species> {
    return request(`/species/${id}`);
}