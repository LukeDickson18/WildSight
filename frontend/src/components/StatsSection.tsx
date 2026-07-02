function StatsSection() {
  const stats = [
    {
      value: "1,204+",
      label: "Sightings Logged",
    },
    {
      value: "563",
      label: "Species Recorded",
    },
    {
      value: "27",
      label: "Birding Hotspots",
    },
    {
      value: "89%",
      label: "Identification Accuracy",
    },
  ];

  return (
    <section className="mx-auto max-w-6xl px-8 pb-20">
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <div
            key={stat.label}
            className="rounded-2xl bg-white p-8 text-center shadow-md transition hover:-translate-y-1 hover:shadow-lg"
          >
            <h2 className="text-4xl font-bold text-green-700">
              {stat.value}
            </h2>

            <p className="mt-2 text-slate-600">
              {stat.label}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default StatsSection;