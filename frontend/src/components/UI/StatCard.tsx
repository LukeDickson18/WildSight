import Card from "./Card";

type StatCardProps = {
  title: string;
  value: string | number;
  description?: string;
};

function StatCard({
  title,
  value,
  description,
}: StatCardProps) {
  return (
    <Card className="text-center">
      <p className="text-sm font-medium text-slate-500">
        {title}
      </p>

      <h2 className="mt-3 text-4xl font-bold text-green-700">
        {value}
      </h2>

      {description && (
        <p className="mt-3 text-sm text-slate-500">
          {description}
        </p>
      )}
    </Card>
  );
}

export default StatCard;