type Sighting = {
  id: number;
  species: string;
  location: string;
  date: string;
};

function RecentSightings() {
  const sightings: Sighting[] = [
    {
      id: 1,
      species: "Cape Sugarbird",
      location: "Table Mountain",
      date: "Today",
    },
    {
      id: 2,
      species: "African Penguin",
      location: "Boulders Beach",
      date: "Yesterday",
    },
    {
      id: 3,
      species: "Malachite Kingfisher",
      location: "Rondevlei Nature Reserve",
      date: "2 days ago",
    },
  ];

  return (
    <section className="mx-auto max-w-6xl px-8 py-20">
      <div className="mb-10 flex items-center justify-between">
        <h2 className="text-3xl font-bold text-slate-900">
          Recent Sightings
        </h2>

        <button className="font-semibold text-green-700 hover:text-green-800">
          View All →
        </button>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {sightings.map((sighting) => (
          <div
            key={sighting.id}
            className="rounded-2xl bg-white p-6 shadow-md transition hover:-translate-y-1 hover:shadow-xl"
          >
            <div className="mb-4 flex h-40 items-center justify-center rounded-xl bg-green-100">
              🌿 Wildlife Photo
            </div>

            <h3 className="text-xl font-semibold">
              {sighting.species}
            </h3>

            <p className="mt-2 text-slate-600">
              📍 {sighting.location}
            </p>

            <p className="mt-2 text-sm text-slate-500">
              {sighting.date}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default RecentSightings;