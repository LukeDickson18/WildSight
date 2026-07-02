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
    "Malachite Kingfisher • Rondevlei",
  ];

  return (
    <main className="mx-auto max-w-7xl px-8 py-10">

      <div className="mb-10">
        <h1 className="text-4xl font-bold">
          Welcome back 👋
        </h1>

        <p className="mt-2 text-slate-600">
          Ready for your next wildlife adventure?
        </p>
      </div>

      <section className="mb-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        {stats.map((stat) => (
          <div
            key={stat.title}
            className="rounded-xl bg-white p-6 shadow"
          >
            <p className="text-slate-500">
              {stat.title}
            </p>

            <h2 className="mt-2 text-3xl font-bold text-green-700">
              {stat.value}
            </h2>
          </div>
        ))}

      </section>

      <section className="mb-10 grid gap-8 lg:grid-cols-3">

        <div className="rounded-xl bg-white p-6 shadow">

          <h2 className="mb-4 text-xl font-semibold">
            Weather Today
          </h2>

          <div className="space-y-2 text-slate-600">
            <p>☀️ Sunny</p>
            <p>22°C</p>
            <p>Wind 11 km/h</p>
          </div>

        </div>

        <div className="rounded-xl bg-white p-6 shadow lg:col-span-2">

          <h2 className="mb-4 text-xl font-semibold">
            Recent Activity
          </h2>

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

        </div>

      </section>

      <section className="mb-10">

        <h2 className="mb-4 text-2xl font-bold">
          Observation Map
        </h2>

        <div className="flex h-96 items-center justify-center rounded-xl border-2 border-dashed border-slate-300 bg-white text-slate-500">
          Interactive map coming soon...
        </div>

      </section>

      <section>

        <h2 className="mb-4 text-2xl font-bold">
          Species Seen This Month
        </h2>

        <div className="flex h-64 items-center justify-center rounded-xl bg-white shadow">
          Charts coming soon...
        </div>

      </section>

    </main>
  );
}

export default DashboardPage;