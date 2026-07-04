import Card from "./ui/Card";

interface Props {
  total: number;
}

export default function ObservationStats({ total }: Props) {
  return (
    <div className="grid gap-4 md:grid-cols-3">
      <Card className="p-5">
        <p className="text-sm text-slate-500">
          Total Observations
        </p>

        <h2 className="mt-2 text-3xl font-bold">
          {total}
        </h2>
      </Card>

      <Card className="p-5">
        <p className="text-sm text-slate-500">
          Species Logged
        </p>

        <h2 className="mt-2 text-3xl font-bold">
          —
        </h2>
      </Card>

      <Card className="p-5">
        <p className="text-sm text-slate-500">
          Locations Visited
        </p>

        <h2 className="mt-2 text-3xl font-bold">
          —
        </h2>
      </Card>
    </div>
  );
}