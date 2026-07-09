import SightingCard from "./SightingsCard";
import type { Sighting } from "../types/Sighting";


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
                    <SightingCard
                        key={sighting.id}
                        sighting={sighting}
                    />
                ))}
            </div>
        </section>
    );
}

export default RecentSightings;