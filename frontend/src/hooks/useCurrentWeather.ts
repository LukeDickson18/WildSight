import { useEffect, useState } from "react";

import { getCurrentWeather } from "../api/weather";

import type { DashboardWeather } from "../types/dashboard";

export function useCurrentWeather(
    latitude: number,
    longitude: number,
) {
    const [weather, setWeather] =
        useState<DashboardWeather | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState<string | null>(null);

    useEffect(() => {
        let cancelled = false;

        async function load() {
            try {
                setLoading(true);

                const response =
                    await getCurrentWeather(
                        latitude,
                        longitude
                    );

                if (!cancelled) {
                    setWeather(response);
                    setError(null);
                }
            } catch {
                if (!cancelled) {
                    setError(
                        "Failed to load weather."
                    );
                }
            } finally {
                if (!cancelled) {
                    setLoading(false);
                }
            }
        }

        load();

        return () => {
            cancelled = true;
        };
    }, [latitude, longitude]);

    return {
        weather,
        loading,
        error,
    };
}