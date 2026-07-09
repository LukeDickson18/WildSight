import { useEffect, useState } from "react";

import WeatherCard from "../weather/WeatherCard";

import { useMap } from "../../context/MapContext";

import { getDashboardWeather } from "../../api/dashboard";
import { useDebounce } from "../../hooks/useDebounce";

import type {
  DashboardWeatherData,
} from "../../types/dashboard";

function DashboardWeather() {
  const { mapLocation } = useMap();
  const debouncedLocation = useDebounce(
    mapLocation,
    500,
  );
  const [weather, setWeather] =
    useState<DashboardWeatherData | null>(null);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {
    async function loadWeather() {
      try {
        setLoading(true);

        const response =
          await getDashboardWeather(
            debouncedLocation.lat,
            debouncedLocation.lng,
          );

        setWeather(response);
      } finally {
        setLoading(false);
      }
    }

    loadWeather();
  }, [debouncedLocation]);

  if (loading || !weather) {
    return (
      <div>
        Loading weather...
      </div>
    );
  }

  return <WeatherCard weather={weather} />;
}

export default DashboardWeather;