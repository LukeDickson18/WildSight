import { useEffect, useState } from "react";

import Card from "../ui/Card";

import { getNearbyHotspots } from "../../api/hotspots";

import { useMap } from "../../context/MapContext";
import { useDebounce } from "../../hooks/useDebounce";

import type { NearbyHotspot } from "../../types/hotspots";

function DashboardNearbyHotspots() {
  const { mapLocation } = useMap();

  const debouncedLocation = useDebounce(
    mapLocation,
    500,
  );

  const [hotspots, setHotspots] = useState<
    NearbyHotspot[]
  >([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadHotspots() {
      try {
        setLoading(true);

        const response =
          await getNearbyHotspots(
            debouncedLocation.lat,
            debouncedLocation.lng,
          );

        setHotspots(response.items);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadHotspots();
  }, [debouncedLocation]);

  return (
    <Card className="h-full">
      <h3 className="mb-4 text-xl font-semibold">
        Nearby Hotspots
      </h3>

      {loading ? (
        <p className="text-slate-500">
          Loading nearby hotspots...
        </p>
      ) : hotspots.length === 0 ? (
        <p className="text-slate-500">
          No hotspots found nearby.
        </p>
      ) : (
        <div className="space-y-3">
          {hotspots.map((hotspot) => (
            <div
              key={hotspot.id}
              className="rounded-lg border border-slate-200 p-4"
            >
              <div className="flex items-center justify-between">
                <h4 className="font-medium">
                  {hotspot.name}
                </h4>

                <span className="text-sm text-slate-500">
                  {hotspot.distance_km.toFixed(1)} km
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

export default DashboardNearbyHotspots;