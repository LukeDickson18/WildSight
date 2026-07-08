import type { DashboardResponse } from "../../types/dashboard";

import StatCard from "../ui/StatCard";

interface Props {
  dashboard: DashboardResponse;
}

function DashboardStats({ dashboard }: Props) {
  const stats = [
    {
      title: "Observations",
      value: dashboard.total_observations,
    },
    {
      title: "Species Seen",
      value: dashboard.species_seen,
    },
    {
      title: "Hotspots Visited",
      value: dashboard.hotspots_visited,
    },
    {
      title: "Countries Visited",
      value: dashboard.countries_visited,
    },
  ];

  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((stat) => (
        <StatCard
          key={stat.title}
          title={stat.title}
          value={stat.value}
        />
      ))}
    </div>
  );
}

export default DashboardStats;