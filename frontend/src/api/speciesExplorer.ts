import { request } from "./client";
import type { ExplorerResponse } from "../types/speciesExplorer";

export function getSpeciesExplorer(): Promise<ExplorerResponse> {
    return request("/species/explorer");
}