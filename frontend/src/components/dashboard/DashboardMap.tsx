import ObservationMap from "../map/ObservationMap";
import FindMeButton from "../map/FindMeButton";

import Card from "../ui/Card";

import { useMap } from "../../context/MapContext";
import { useCurrentLocation } from "../../hooks/useCurrentLocation";

function DashboardMap() {
  const { mapLocation, setMapLocation } = useMap();

  const { findMe } = useCurrentLocation();

  async function handleFindMe() {
    const location = await findMe();

    if (location) {
      setMapLocation(location);
    }
  }

  return (
    <Card className="overflow-hidden p-0">
      <div className="relative">
        <ObservationMap
          position={mapLocation}
          onPositionChange={setMapLocation}
        />

        <div className="absolute top-4 right-4 z-[1000]">
          <FindMeButton onClick={handleFindMe} />
        </div>
      </div>
    </Card>
  );
}

export default DashboardMap;