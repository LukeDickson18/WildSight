export interface ExplorerSpecies {
    id: string;
    common_name: string;
    image_url: string | null;
    thumbnail_url: string | null;
}

export interface ExplorerGroup {
    name: string;
    scientific_name: string;
    species: ExplorerSpecies[];
}

export interface ExplorerResponse {
    groups: ExplorerGroup[];
}