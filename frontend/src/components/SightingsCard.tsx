import type { Sighting } from "../types/Sighting";

type SightingCardProps = {
  sighting: Sighting;
};

function SightingCard({ sighting }: SightingCardProps) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md transition hover:-translate-y-1 hover:shadow-xl">
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
  );
}

export default SightingCard;