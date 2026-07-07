import {
  Calendar,
  MapPin,
  Trash2,
  Users,
} from "lucide-react";

import type { Observation } from "../../types/observation";

import Card from "../ui/Card";
import Button from "../ui/Button";

interface ObservationCardProps {
  observation: Observation;
  onDelete: (id: string) => void;
}

export default function ObservationCard({
  observation,
  onDelete,
}: ObservationCardProps) {
  const observationDate = new Date(
    observation.observation_datetime,
  );

  return (
    <Card className="transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
      <div className="flex items-start justify-between p-6">
        <div className="min-w-0 flex-1">

          <h2 className="text-xl font-semibold text-slate-900">
            {observation.species.common_name}
          </h2>

          <p className="mt-1 italic text-slate-500">
            {observation.species.scientific_name}
          </p>

          <div className="mt-5 flex flex-wrap gap-x-6 gap-y-2 text-sm text-slate-600">

            <div className="flex items-center gap-2">
              <Calendar className="h-4 w-4" />
              <span>
                {observationDate.toLocaleDateString()} •{" "}
                {observationDate.toLocaleTimeString([], {
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </span>
            </div>

            <div className="flex items-center gap-2">
              <MapPin className="h-4 w-4" />
              <span>
                {observation.location?.name ??
                  "Unknown location"}
              </span>
            </div>

            <div className="flex items-center gap-2">
              <Users className="h-4 w-4" />
              <span>
                {observation.count} individual
                {observation.count !== 1 && "s"}
              </span>
            </div>

          </div>

          {observation.notes && (
            <p className="mt-5 line-clamp-2 text-sm leading-6 text-slate-700">
              {observation.notes}
            </p>
          )}

        </div>

        <Button
          variant="danger"
          onClick={() =>
            onDelete(observation.id)
          }
        >
          <Trash2 className="h-4 w-4" />
        </Button>
      </div>
    </Card>
  );
}