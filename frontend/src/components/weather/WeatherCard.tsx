import Card from "../ui/Card";

import type { DashboardWeather } from "../../types/dashboard";

type DashboardWeatherCardProps = {
  weather: DashboardWeather;
};

function DashboardWeatherCard({
  weather,
}: DashboardWeatherCardProps) {
  return (
    <Card>
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-xl font-semibold">
            Current Conditions
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            Live weather
          </p>
        </div>

        <div className="text-right">
          <p className="text-4xl font-bold text-slate-900">
            {weather.temperature.toFixed(1)}°
          </p>

          <p className="text-slate-600">
            {weather.weather_description}
          </p>
        </div>
      </div>

      <div className="mt-8 grid grid-cols-2 gap-4">
        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Feels Like
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.apparent_temperature.toFixed(1)}°C
          </p>
        </div>

        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Humidity
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.relative_humidity}%
          </p>
        </div>

        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Wind
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.wind_speed} km/h
          </p>
        </div>

        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Rain
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.precipitation} mm
          </p>
        </div>

        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Cloud Cover
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.cloud_cover}%
          </p>
        </div>

        <div className="rounded-lg bg-slate-50 p-4">
          <p className="text-sm text-slate-500">
            Wind Direction
          </p>

          <p className="mt-1 text-lg font-semibold">
            {weather.wind_direction}°
          </p>
        </div>
      </div>
    </Card>
  );
}

export default DashboardWeatherCard;