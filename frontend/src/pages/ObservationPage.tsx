import { useMemo } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import PageHeader from "../components/ui/PageHeader";
import Card from "../components/ui/Card";

import ObservationToolbar from "../components/observations/ObservationToolbar";
import ObservationSummary from "../components/observations/ObservationSummary";
import ObservationGroup from "../components/observations/ObservationGroup";
import ObservationPagination from "../components/observations/ObservationPagination";
import ObservationEmptyState from "../components/observations/ObservationEmptyState";

import { useObservations } from "../hooks/useObservations";

import { deleteObservation } from "../api/observation";
import { useAuth } from "../auth/useAuth";

import { groupObservations } from "../utils/observationGrouping";

export default function ObservationsPage() {
  const navigate = useNavigate();

  const { token } = useAuth();

  const {
    observations,
    loading,
    error,

    total,
    totalPages,

    page,
    pageSize,

    search,
    setSearch,

    setPage,

    refresh,
  } = useObservations();

  const groups = useMemo(
    () => groupObservations(observations),
    [observations],
  );

  async function handleDelete(id: string) {
    if (!token) return;

    const confirmed = window.confirm(
      "Delete this observation?",
    );

    if (!confirmed) return;

    try {
      await deleteObservation(id, token);

      await refresh();
    } catch (err) {
      console.error(err);

      alert(
        "Unable to delete observation.",
      );
    }
  }

  return (
    <MainLayout>
      <div className="space-y-8">

        <PageHeader
          title="My Observations"
          description="Browse, search and manage your wildlife observations."
        />

        <ObservationToolbar
          search={search}
          onSearchChange={setSearch}
        />

        <ObservationSummary
          total={total}
          page={page}
          pageSize={pageSize}
        />

        {loading && (
          <Card className="p-10 text-center">
            Loading observations...
          </Card>
        )}

        {!loading && error && (
          <Card className="p-10 text-center text-red-600">
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
              <div className="space-y-10">
                {groups.map((group) => (
                  <ObservationGroup
                    key={group.title}
                    title={group.title}
                    observations={
                      group.observations
                    }
                    onDelete={handleDelete}
                  />
                ))}
              </div>

              <ObservationPagination
                page={page}
                totalPages={totalPages}
                onPageChange={setPage}
              />
            </>
          )}

      </div>
    </MainLayout>
  );
}