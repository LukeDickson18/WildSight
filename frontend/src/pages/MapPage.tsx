import ObservationMap from "../components/map/ObservationMap";
import FindMeButton from "../components/map/FindMeButton";
import DashboardWeatherCard from "../components/weather/WeatherCard";

import { useCurrentLocation } from "../hooks/useCurrentLocation";
import { useCurrentWeather } from "../hooks/useCurrentWeather";
import { useMap } from "../context/MapContext";

function MapPage() {
  const { mapLocation, setMapLocation } = useMap();

  const { findMe } = useCurrentLocation();

  const {
    weather,
    loading,
    error,
  } = useCurrentWeather(
    mapLocation.lat,
    mapLocation.lng
  );

  async function handleFindMe() {
    try {
      const location = await findMe();

      setMapLocation({
        lat: location.coords.latitude,
        lng: location.coords.longitude,
      });
    } catch (err) {
      console.error("Unable to retrieve location.", err);
    }
  }

  return (
    <div className="mx-auto max-w-7xl space-y-6 p-6">

      <div className="flex justify-end">
        <FindMeButton onClick={handleFindMe} />
      </div>

      <ObservationMap
        position={mapLocation}
        onPositionChange={setMapLocation}
      />

      <div className="grid gap-6 lg:grid-cols-2">

        <div className="rounded-lg border bg-white p-4">
          <h2 className="mb-4 text-lg font-semibold">
            Selected Location
          </h2>

          <div className="space-y-2">
            <p>
              <span className="font-medium">
                Latitude:
              </span>{" "}
              {mapLocation.lat.toFixed(6)}
            </p>

            <p>
              <span className="font-medium">
                Longitude:
              </span>{" "}
              {mapLocation.lng.toFixed(6)}
            </p>
          </div>
        </div>

        <div>
          {loading && (
            <div className="rounded-lg border bg-white p-6">
              Loading weather...
            </div>
          )}

          {error && (
            <div className="rounded-lg border border-red-300 bg-red-50 p-6 text-red-600">
              {error}
            </div>
          )}

          {weather && (
            <DashboardWeatherCard weather={weather} />
          )}
        </div>

      </div>

    </div>
  );
}

export default MapPage;