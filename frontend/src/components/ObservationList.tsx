import type { Observation } from "../types/observation";
import ObservationCard from "./ObservationCard";

interface Props {
  observations: Observation[];
  onDelete: (id: string) => void;
}

export default function ObservationList({
  observations,
  onDelete,
}: Props) {
  return (
    <div className="space-y-4">
      {observations.map((observation) => (
        <ObservationCard
          key={observation.id}
          observation={observation}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}