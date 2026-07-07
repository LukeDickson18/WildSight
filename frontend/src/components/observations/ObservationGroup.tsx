import type { Observation } from "../../types/observation";

import ObservationCard from "./ObservationCard";

interface ObservationGroupProps {
  title: string;
  observations: Observation[];
  onDelete: (id: string) => void;
}

export default function ObservationGroup({
  title,
  observations,
  onDelete,
}: ObservationGroupProps) {
  return (
    <section className="space-y-4">
      <div className="sticky top-0 z-10 bg-slate-50 py-2">
        <h2 className="text-lg font-semibold text-slate-900">
          {title}
        </h2>
      </div>

      <div className="space-y-4">
        {observations.map((observation) => (
          <ObservationCard
            key={observation.id}
            observation={observation}
            onDelete={onDelete}
          />
        ))}
      </div>
    </section>
  );
}