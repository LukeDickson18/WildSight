import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { useAuth } from "../auth/useAuth";
import { getDashboard } from "../api/dashboard";

import type { DashboardResponse } from "../types/dashboard";

import Card from "../components/ui/Card";
import Divider from "../components/ui/Divider";
import PageHeader from "../components/ui/PageHeader";
import Section from "../components/ui/Section";

import DashboardStats from "../components/dashboard/DashboardStats";
import DashboardMap from "../components/dashboard/DashboardMap";
import DashboardWeather from "../components/dashboard/DashboardWeather";
import DashboardNearbyHotspots from "../components/dashboard/DashboardNearbyHotspots";
import DashboardAnalytics from "../components/dashboard/DashboardAnalytics";

import RecentObservations from "../components/RecentObservations";

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

  if (error || !dashboard) {
    return (
      <MainLayout>
        <PageHeader title="Dashboard" />

        <Card className="p-8 text-center text-red-600">
          {error ?? "Unable to load dashboard."}
        </Card>
      </MainLayout>
    );
  }

  return (
    <MainLayout>
      <PageHeader
        title="Dashboard"
        subtitle="Ready for your next wildlife adventure?"
      />

      <Section title="Overview">
        <DashboardStats dashboard={dashboard} />
      </Section>

      <Divider />

      <Section title="Interactive Observation Map">
        <DashboardMap />
      </Section>

      <Divider />

      <Section title="Current Conditions">
        <div className="grid gap-6 lg:grid-cols-3">
          <DashboardWeather
            weather={dashboard.weather}
          />

          <div className="lg:col-span-2">
            <DashboardNearbyHotspots />
          </div>
        </div>
      </Section>

      <Divider />

      <Section title="Analytics">
        <DashboardAnalytics />
      </Section>
    </MainLayout>
  );
}

export default DashboardPage;