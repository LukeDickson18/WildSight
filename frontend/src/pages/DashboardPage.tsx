import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { useAuth } from "../auth/useAuth";
import { getDashboard } from "../api/dashboard";

import type { DashboardResponse } from "../types/dashboard";

import Card from "../components/ui/Card";
import Divider from "../components/ui/Divider";
import PageHeader from "../components/ui/PageHeader";
import Section from "../components/ui/Section";
import StatCard from "../components/ui/StatCard";

import MapPreview from "../components/MapPreview";
import RecentSightings from "../components/RecentSightings";

function DashboardPage() {
  const { token } = useAuth();

  const [dashboard, setDashboard] =
    useState<DashboardResponse | null>(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] =
    useState<string | null>(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const response = await getDashboard(token);

        setDashboard(response);
      } catch (err) {
        console.error(err);
        setError("Unable to load dashboard.");
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, [token]);

  if (loading) {
    return (
      <MainLayout>
        <PageHeader
          title="Dashboard"
          subtitle="Loading dashboard..."
        />
      </MainLayout>
    );
  }

  if (error) {
    return (
      <MainLayout>
        <PageHeader title="Dashboard" />

        <Card className="p-8 text-center text-red-600">
          {error}
        </Card>
      </MainLayout>
    );
  }

  const stats = [
    {
      title: "Observations",
      value: dashboard?.total_observations ?? 0,
    },
    {
      title: "Species Seen",
      value: dashboard?.species_seen ?? 0,
    },
    {
      title: "Hotspots Visited",
      value: dashboard?.hotspots_visited ?? 0,
    },
    {
      title: "Countries Visited",
      value: dashboard?.countries_visited ?? 0,
    },
  ];

  const recentActivity = [
    "Recent observations coming soon...",
  ];

  return (
    <MainLayout>
      <PageHeader
        title="Dashboard"
        subtitle="Ready for your next wildlife adventure?"
      />

      <Section title="Overview">
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {stats.map((stat) => (
            <StatCard
              key={stat.title}
              title={stat.title}
              value={stat.value}
            />
          ))}
        </div>
      </Section>

      <Divider />

      <Section title="Today's Summary">
        <div className="grid gap-6 lg:grid-cols-3">
          <Card>
            <h3 className="mb-4 text-xl font-semibold">
              Weather Today
            </h3>

            <div className="space-y-2 text-slate-600">
              <p>☀️ Coming Soon</p>
              <p>Environmental enrichment will appear here.</p>
            </div>
          </Card>

          <Card className="lg:col-span-2">
            <h3 className="mb-4 text-xl font-semibold">
              Recent Activity
            </h3>

            <ul className="space-y-3">
              {recentActivity.map((activity) => (
                <li
                  key={activity}
                  className="rounded-lg bg-slate-100 p-3"
                >
                  {activity}
                </li>
              ))}
            </ul>
          </Card>
        </div>
      </Section>

      <Divider />

      <Section title="Observation Map">
        <MapPreview />
      </Section>

      <Divider />

      <Section title="Recent Sightings">
        <RecentSightings />
      </Section>

      <Divider />

      <Section title="Species Analytics">
        <Card className="flex h-64 items-center justify-center">
          <p className="text-slate-500">
            Analytics coming soon...
          </p>
        </Card>
      </Section>
    </MainLayout>
  );
}

export default DashboardPage;