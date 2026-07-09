import { keepPreviousData, useQuery } from "@tanstack/react-query";

import { getSpeciesExplorer } from "../api/speciesExplorer";

import type { SpeciesExplorerFilters } from "../types/speciesFilters";

export function useSpeciesExplorer(
    filters: SpeciesExplorerFilters,
) {
    return useQuery({
        queryKey: ["speciesExplorer", filters],
        queryFn: () => getSpeciesExplorer(filters),
        placeholderData: keepPreviousData,
    });
}