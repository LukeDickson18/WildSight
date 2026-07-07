import { useCallback, useEffect, useState } from "react";

import { getObservations } from "../api/observation";
import { useAuth } from "../auth/useAuth";

import type {
  Observation,
  ObservationSort,
} from "../types/observation";

export function useObservations() {
  const { token } = useAuth();

  const [observations, setObservations] = useState<Observation[]>([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState<string | null>(null);

  const [page, setPage] = useState(1);

  const [pageSize] = useState(25);

  const [total, setTotal] = useState(0);

  const [totalPages, setTotalPages] = useState(1);

  const [search, setSearch] = useState("");

  const [speciesId, setSpeciesId] = useState<string>();

  const [startDate, setStartDate] = useState("");

  const [endDate, setEndDate] = useState("");

  const [sort, setSort] =
    useState<ObservationSort>("newest");

  const loadObservations = useCallback(async () => {
    if (!token) {
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await getObservations({
        page,
        pageSize,
        search: search || undefined,
        speciesId,
        startDate: startDate || undefined,
        endDate: endDate || undefined,
        sort,
        token,
      });

      setObservations(response.items);

      setTotal(response.total);

      setTotalPages(response.total_pages);
    } catch (err) {
      console.error(err);

      setError(
        "Unable to load observations.",
      );
    } finally {
      setLoading(false);
    }
  }, [
    token,
    page,
    pageSize,
    search,
    speciesId,
    startDate,
    endDate,
    sort,
  ]);

  useEffect(() => {
    loadObservations();
  }, [loadObservations]);

  return {
    observations,

    loading,

    error,

    total,

    totalPages,

    page,

    pageSize,

    search,

    speciesId,

    startDate,

    endDate,

    sort,

    setPage,

    setSearch,

    setSpeciesId,

    setStartDate,

    setEndDate,

    setSort,

    refresh: loadObservations,
  };
}