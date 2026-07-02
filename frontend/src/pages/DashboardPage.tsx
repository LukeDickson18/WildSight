import MainLayout from "../layouts/MainLayout";

import Card from "../components/ui/Card";
import Divider from "../components/ui/Divider";
import PageHeader from "../components/ui/PageHeader";
import Section from "../components/ui/Section";
import StatCard from "../components/ui/StatCard";

import MapPreview from "../components/MapPreview";
import RecentSightings from "../components/RecentSightings";

function DashboardPage() {
  const stats = [
    {
      title: "Sightings",
      value: "143",
    },
    {
      title: "Species",
      value: "61",
    },
    {
      title: "Hotspots",
      value: "8",
    },
    {
      title: "Current Streak",
      value: "12 Days",
    },
  ];

  const recentActivity = [
    "Cape Sugarbird • Table Mountain",
    "African Penguin • Boulders Beach",
    "Malachite Kingfisher • Rondevlei Nature Reserve",
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
              <p>☀️ Sunny</p>
              <p>22°C</p>
              <p>Wind: 11 km/h</p>
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
            Charts coming soon...
          </p>
        </Card>
      </Section>
    </MainLayout>
  );
}

export default DashboardPage;