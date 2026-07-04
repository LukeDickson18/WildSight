import { useCallback, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Button from "../components/ui/Button";
import Card from "../components/ui/Card";
import PageHeader from "../components/ui/PageHeader";

import ObservationList from "../components/ObservationList";
import ObservationEmptyState from "../components/ObservationEmptyState";
import ObservationStats from "../components/ObservationStats";

import {
  deleteObservation,
  getObservations,
} from "../api/observation";

import { useAuth } from "../auth/useAuth";

import type {
  Observation,
  ObservationListResponse,
} from "../types/observation";

export default function ObservationsPage() {
  const navigate = useNavigate();
  const { token } = useAuth();

  const [observations, setObservations] = useState<Observation[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);

  const pageSize = 50;

  const loadObservations = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const response: ObservationListResponse =
        await getObservations(page, pageSize, token);

      setObservations(response.items);
      setTotal(response.total);
    } catch (err) {
      console.error(err);
      setError("Failed to load observations.");
    } finally {
      setLoading(false);
    }
  }, [page, token]);

  useEffect(() => {
    loadObservations();
  }, [loadObservations]);

  async function handleRefresh() {
    setRefreshing(true);

    await loadObservations();

    setRefreshing(false);
  }

  async function handleDelete(id: string) {
    if (!token) return;

    const confirmed = window.confirm(
      "Delete this observation?"
    );

    if (!confirmed) return;

    try {
      await deleteObservation(id, token);

      await loadObservations();
    } catch (err) {
      console.error(err);
      alert("Unable to delete observation.");
    }
  }

  return (
    <MainLayout>
      <div className="space-y-8">

        <PageHeader
          title="Observations"
          description="Record, review and manage your wildlife observations."
        />

        <div className="flex flex-wrap gap-4 justify-between">

          <Button
            onClick={() =>
              navigate("/observations/new")
            }
          >
            Log Observation
          </Button>

          <Button
            variant="secondary"
            onClick={handleRefresh}
            disabled={refreshing}
          >
            {refreshing
              ? "Refreshing..."
              : "Refresh"}
          </Button>

        </div>

        <ObservationStats
          total={total}
        />

        {loading && (
          <Card className="p-8 text-center">
            Loading observations...
          </Card>
        )}

        {error && (
          <Card className="p-8 text-center text-red-600">
            {error}
          </Card>
        )}

        {!loading &&
          !error &&
          observations.length === 0 && (
            <ObservationEmptyState
              onCreate={() =>
                navigate("/observations/new")
              }
            />
          )}

        {!loading &&
          !error &&
          observations.length > 0 && (
            <>
              <ObservationList
                observations={observations}
                onDelete={handleDelete}
              />

              <div className="flex justify-between items-center pt-4">

                <Button
                  disabled={page === 1}
                  onClick={() =>
                    setPage((p) => p - 1)
                  }
                >
                  Previous
                </Button>

                <span className="text-sm text-slate-600">
                  Page {page}
                </span>

                <Button
                  disabled={observations.length < pageSize}
                  onClick={() =>
                    setPage((p) => p + 1)
                  }
                >
                  Next
                </Button>

              </div>
            </>
          )}

      </div>
    </MainLayout>
  );
}