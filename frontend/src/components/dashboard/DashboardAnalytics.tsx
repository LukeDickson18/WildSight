import Card from "../ui/Card";

function DashboardAnalytics() {
  return (
    <Card className="flex h-72 items-center justify-center">
      <div className="text-center">
        <h3 className="text-xl font-semibold">
          Analytics
        </h3>

        <p className="mt-2 text-slate-500">
          Observation trends, heatmaps and prediction
          models (likely birds, etc) will appear here in a future update.
        </p>
      </div>
    </Card>
  );
}

export default DashboardAnalytics;