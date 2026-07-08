import { useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import SpeciesExplorer from "../components/species/SpeciesExplorer";
import SpeciesFilters from "../components/species/SpeciesFilter";
import SpeciesSearchBar from "../components/species/SpeciesSearchBar";

import Container from "../components/ui/Container";
import PageHeader from "../components/ui/PageHeader";

import {
    defaultSpeciesFilters,
    type SpeciesFilters as SpeciesFiltersType,
} from "../types/speciesFilters";

function SpeciesPage() {
    const navigate = useNavigate();

    const [filters, setFilters] =
        useState<SpeciesFiltersType>(
            defaultSpeciesFilters
        );

    function updateFilter<
        K extends keyof SpeciesFiltersType
    >(key: K, value: SpeciesFiltersType[K]) {
        setFilters((previous) => ({
            ...previous,
            [key]: value,
        }));
    }

    function handleSearch() {
        console.log(filters);

        // Future:
        // searchSpecies(filters)
    }

    return (
        <MainLayout>
            <Container>
                <PageHeader
                    title="Species Explorer"
                    subtitle="Browse the birds of Southern Africa by taxonomic order."
                />

                <SpeciesFilters
                    useMyLocation={filters.useMyLocation}
                    radius={filters.radius}
                    country={filters.country}
                    hotspot={filters.hotspot}
                    onUseMyLocationChange={(value) =>
                        updateFilter(
                            "useMyLocation",
                            value
                        )
                    }
                    onRadiusChange={(value) =>
                        updateFilter("radius", value)
                    }
                    onCountryChange={(value) =>
                        updateFilter("country", value)
                    }
                    onHotspotChange={(value) =>
                        updateFilter("hotspot", value)
                    }
                />

                <SpeciesSearchBar
                    value={filters.search}
                    onChange={(value) =>
                        updateFilter("search", value)
                    }
                    onSearch={handleSearch}
                />

                <SpeciesExplorer
                    onSpeciesClick={(species) =>
                        navigate(`/species/${species.id}`)
                    }
                />
            </Container>
        </MainLayout>
    );
}

export default SpeciesPage;