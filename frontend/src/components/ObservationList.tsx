import type { Observation } from "../types/observation";
import ObservationCard from "./ObservationCard";

interface Props {
  observations: Observation[];
}

export default function ObservationList({
  observations,
}: Props) {
  return (
    <div className="space-y-4">
      {observations.map((observation) => (
        <ObservationCard
          key={observation.id}
          observation={observation}
        />
      ))}
    </div>
  );
}