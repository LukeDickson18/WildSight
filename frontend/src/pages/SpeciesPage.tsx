import { useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import SpeciesExplorer from "../components/species/SpeciesExplorer";
import SpeciesFilters from "../components/species/SpeciesFilter";
import SpeciesSearchBar from "../components/species/SpeciesSearchBar";

import Container from "../components/ui/Container";
import PageHeader from "../components/ui/PageHeader";

import { useSpeciesExplorer } from "../hooks/useSpeciesExplorer";

import {
    defaultSpeciesFilters,
    type SpeciesFilterState,
    type SpeciesExplorerFilters,
} from "../types/speciesFilters";

function SpeciesPage() {
    const navigate = useNavigate();

    const [uiFilters, setFilters] =
        useState<SpeciesFilterState>(defaultSpeciesFilters);

    const [apiFilters, setAppliedFilters] =
        useState<SpeciesExplorerFilters>({
            page: 1,
            pageSize: 25,
        });

    const {
        data,
        isLoading,
        error,
    } = useSpeciesExplorer(apiFilters);

    function updateFilter<
        K extends keyof SpeciesFilterState
    >(key: K, value: SpeciesFilterState[K]) {
        setFilters((previous) => ({
            ...previous,
            [key]: value,
        }));
    }

    function handleSearch() {
        setAppliedFilters({
            search: uiFilters.search,
            page: 1,
            pageSize: 25,
        });
    }

    return (
        <MainLayout>
            <Container>
                <PageHeader
                    title="Species Explorer"
                    subtitle="Browse the birds of Southern Africa by taxonomic order."
                />

                <SpeciesFilters
                    useMyLocation={uiFilters.useMyLocation}
                    radius={uiFilters.radius}
                    country={uiFilters.country}
                    hotspot={uiFilters.hotspot}
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
                    value={uiFilters.search}
                    onChange={(value) =>
                        updateFilter("search", value)
                    }
                    onSearch={handleSearch}
                />

                <SpeciesExplorer
                    species={data?.items ?? []}
                    loading={isLoading}
                    error={error?.message ?? ""}
                    onSpeciesClick={(species) =>
                        navigate(`/species/${species.id}`)
                    }
                />
            </Container>
        </MainLayout>
    );
}

export default SpeciesPage;