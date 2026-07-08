import Card from "../ui/Card";

function DashboardNearbyHotspots() {
  return (
    <Card className="h-full">
      <h3 className="mb-4 text-xl font-semibold">
        Nearby Hotspots
      </h3>

      <div className="space-y-3">
        <div className="rounded-lg bg-slate-100 p-4">
          <p className="font-medium">
            Hotspots coming soon
          </p>

          <p className="text-sm text-slate-500">
            Nearby hotspots within 10 km will appear here.
          </p>
        </div>
      </div>
    </Card>
  );
}

export default DashboardNearbyHotspots;