import { request } from "./client";

import type {
    Species,
} from "../types/species";


export function getSpeciesById(
    id: string,
): Promise<Species> {
    return request(`/species/${id}`);
}