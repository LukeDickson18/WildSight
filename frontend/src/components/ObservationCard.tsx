import type { Observation } from "../types/observation";
import Card from "./ui/Card";

interface Props {
  observation: Observation;
}

export default function ObservationCard({ observation }: Props) {
  return (
    <Card className="p-6 hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start">
        <div>
          <h2 className="text-xl font-semibold">
            {observation.species.common_name}
          </h2>

          <p className="text-sm italic text-slate-500">
            {observation.species.scientific_name}
          </p>

          <div className="mt-4 space-y-1 text-sm text-slate-600">
            <p>
              <span className="font-medium">Location:</span>{" "}
              {observation.location.name}
            </p>

            <p>
              <span className="font-medium">Count:</span>{" "}
              {observation.count}
            </p>

            <p>
              <span className="font-medium">Observer:</span>{" "}
              {observation.user.username}
            </p>
          </div>

          {observation.notes && (
            <p className="mt-4 text-sm text-slate-700">
              {observation.notes}
            </p>
          )}
        </div>

        <div className="text-right text-sm text-slate-500">
          {new Date(
            observation.observation_datetime,
          ).toLocaleDateString()}
        </div>
      </div>
    </Card>
  );
}