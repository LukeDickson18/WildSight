export interface Order {
    id: string;
    name: string;
}

export interface Family {
    id: string;
    family_code: string;
    common_name: string;
    scientific_name: string;
    order: Order;
}

export interface Species {
    id: string;
    ebird_code: string;
    common_name: string;
    scientific_name: string;
    category: string;
    wildlife_group: string;

    // iNaturalist
    inat_taxon_id: number | null;
    image_url: string | null;
    thumbnail_url: string | null;
    image_license: string | null;
    image_attribution: string | null;
    image_source: string | null;

    family: Family;
}

export interface SpeciesExplorerSpecies {
    id: string;

    common_name: string;
    scientific_name: string;

    image_url: string | null;
    thumbnail_url: string | null;

    family_common_name: string | null;
    order_common_name: string | null;
}

export interface SpeciesExplorerResponse {
    items: SpeciesExplorerSpecies[];
    total: number;
    page: number;
    page_size: number;
}

export interface SpeciesListResponse {
    items: Species[];
    total: number;
    page: number;
    page_size: number;
}