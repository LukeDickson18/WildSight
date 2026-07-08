import WeatherCard from "../weather/WeatherCard";

import type { DashboardWeatherData } from "../../types/dashboard";

type Props = {
  weather: DashboardWeatherData;
};

function DashboardWeather({ weather }: Props) {
  return <WeatherCard weather={weather} />;
}

export default DashboardWeather;