export type SpeciesFilters = {
    search: string;
    useMyLocation: boolean;
    radius: string;
    country: string;
    hotspot: string;
};

export const defaultSpeciesFilters: SpeciesFilters = {
    search: "",
    useMyLocation: false,
    radius: "50",
    country: "South Africa",
    hotspot: "Any",
};