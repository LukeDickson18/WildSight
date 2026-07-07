import Card from "../ui/Card";

interface ObservationSummaryProps {
  total: number;
  page: number;
  pageSize: number;
}

export default function ObservationSummary({
  total,
  page,
  pageSize,
}: ObservationSummaryProps) {
  const start =
    total === 0
      ? 0
      : (page - 1) * pageSize + 1;

  const end = Math.min(
    page * pageSize,
    total,
  );

  return (
    <Card className="p-5">
      <div className="flex flex-col gap-1 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">
            My Observations
          </h2>

          <p className="text-sm text-slate-500">
            Showing{" "}
            <span className="font-medium">
              {start}-{end}
            </span>{" "}
            of{" "}
            <span className="font-medium">
              {total}
            </span>{" "}
            observations
          </p>
        </div>

        <div className="text-sm text-slate-500">
          Page{" "}
          <span className="font-medium">
            {page}
          </span>
        </div>
      </div>
    </Card>
  );
}