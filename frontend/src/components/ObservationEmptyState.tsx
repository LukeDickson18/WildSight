import Button from "./ui/Button";

interface Props {
  onCreate: () => void;
}

export default function ObservationEmptyState({
  onCreate,
}: Props) {
  return (
    <div className="rounded-xl border-2 border-dashed border-slate-300 bg-white p-12 text-center">
      <h2 className="text-2xl font-semibold">
        No observations yet
      </h2>

      <p className="mt-3 text-slate-500">
        Start building your wildlife journal by logging your first observation.
      </p>

      <Button
        className="mt-6"
        onClick={onCreate}
      >
        Log Observation
      </Button>
    </div>
  );
}