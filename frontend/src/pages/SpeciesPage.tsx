import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import SpeciesExplorer from "../components/species/SpeciesExplorer";
import SpeciesFilters from "../components/species/SpeciesExplorerFilter";
import SpeciesSearchBar from "../components/species/SpeciesSearchBar";

import Container from "../components/ui/Container";
import PageHeader from "../components/ui/PageHeader";

import { useSpeciesExplorer } from "../hooks/useSpeciesExplorer";
import { useCurrentLocation } from "../hooks/useCurrentLocation";

import {
  defaultSpeciesFilters,
  type SpeciesExplorerFilters,
  type SpeciesFilterState,
} from "../types/speciesFilters";

function SpeciesPage() {
  const navigate = useNavigate();

  const [uiFilters, setUiFilters] =
    useState<SpeciesFilterState>(defaultSpeciesFilters);

  const [apiFilters, setApiFilters] =
    useState<SpeciesExplorerFilters>({
      page: 1,
      pageSize: 25,
    });

  const {
    data,
    isLoading,
    error,
  } = useSpeciesExplorer(apiFilters);

  const { findMe } = useCurrentLocation();

  function updateFilter<
    K extends keyof SpeciesFilterState,
  >(key: K, value: SpeciesFilterState[K]) {
    setUiFilters((previous) => ({
      ...previous,
      [key]: value,
    }));
  }

  function buildExplorerFilters(): SpeciesExplorerFilters {
    return {
      search: uiFilters.search || undefined,

      countryId: uiFilters.countryId || undefined,
      orderId: uiFilters.orderId || undefined,
      familyId: uiFilters.familyId || undefined,

      latitude: uiFilters.latitude,
      longitude: uiFilters.longitude,
      radiusKm: Number(uiFilters.radius),

      hotspotId: uiFilters.hotspotId || undefined,

      page: 1,
      pageSize: 25,
    };
  }

  function handleSearch() {
    setApiFilters(buildExplorerFilters());
  }

  useEffect(() => {
    async function loadLocation() {
      if (!uiFilters.useMyLocation) {
        updateFilter("latitude", undefined);
        updateFilter("longitude", undefined);
        return;
      }

      try {
        const location = await findMe();

        updateFilter("latitude", location.lat);
        updateFilter("longitude", location.lng);
      } catch (error) {
        console.error(
          "Failed to get current location:",
          error,
        );

        updateFilter("useMyLocation", false);
        updateFilter("latitude", undefined);
        updateFilter("longitude", undefined);
      }
    }

    loadLocation();
  }, [uiFilters.useMyLocation, findMe]);

  useEffect(() => {
    const filters = buildExplorerFilters();

    setApiFilters((previous) => ({
      ...filters,
      search: previous.search,
    }));
  }, [
    uiFilters.countryId,
    uiFilters.orderId,
    uiFilters.familyId,
    uiFilters.hotspotId,
    uiFilters.latitude,
    uiFilters.longitude,
    uiFilters.radius,
    uiFilters.useMyLocation,
  ]);

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
          country={uiFilters.countryId}
          order={uiFilters.orderId}
          family={uiFilters.familyId}
          hotspot={uiFilters.hotspotId}
          onUseMyLocationChange={(value) =>
            updateFilter("useMyLocation", value)
          }
          onRadiusChange={(value) =>
            updateFilter("radius", value)
          }
          onCountryChange={(value) =>
            updateFilter("countryId", value)
          }
          onOrderChange={(value) =>
            updateFilter("orderId", value)
          }
          onFamilyChange={(value) =>
            updateFilter("familyId", value)
          }
          onHotspotChange={(value) =>
            updateFilter("hotspotId", value)
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