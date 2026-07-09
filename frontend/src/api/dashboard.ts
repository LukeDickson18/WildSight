import { request } from "./client";

import type {
    DashboardResponse,
    DashboardWeatherData,
} from "../types/dashboard";

export async function getDashboard(
    token?: string | null,
): Promise<DashboardResponse> {
    return request("/dashboard", {
        token,
    });
}

export async function getDashboardWeather(
    latitude: number,
    longitude: number,
): Promise<DashboardWeatherData> {
    return request(
        `/dashboard/weather?lat=${latitude}&lon=${longitude}`
    );
}