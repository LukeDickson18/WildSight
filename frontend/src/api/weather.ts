import { request } from "./client";

import type { DashboardWeather } from "../types/dashboard";

export function getCurrentWeather(
  latitude: number,
  longitude: number
) {
  return request<DashboardWeather>(
    `/weather/current?latitude=${latitude}&longitude=${longitude}`
  );
}