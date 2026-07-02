import Card from "./ui/Card";
import Button from "./ui/Button";

function MapPreview() {
  return (
    <Card>
      <div className="flex h-80 flex-col items-center justify-center rounded-xl border-2 border-dashed border-slate-300 bg-slate-50 text-center">
        <div className="mb-4 text-6xl">🗺️</div>

        <h3 className="text-2xl font-semibold text-slate-800">
          Interactive Observation Map
        </h3>

        <p className="mt-3 max-w-md text-slate-600">
          Explore wildlife sightings, birding hotspots, and your own
          observations on an interactive map. This feature will be powered by
          Leaflet and PostGIS in a future release.
        </p>

        <Button className="mt-8" variant="secondary">
          Coming Soon
        </Button>
      </div>
    </Card>
  );
}

export default MapPreview;