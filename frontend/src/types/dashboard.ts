export interface DashboardWeatherData {
  temperature: number;
  apparent_temperature: number;
  relative_humidity: number;

  wind_speed: number;
  wind_direction: number;

  cloud_cover: number;
  precipitation: number;

  weather_description: string;
}

export interface DashboardResponse {
  total_observations: number;
  species_seen: number;
  hotspots_visited: number;
  countries_visited: number;

  weather: DashboardWeatherData;
}