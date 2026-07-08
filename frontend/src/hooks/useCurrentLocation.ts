import { useCallback } from "react";

import type { LatLngLiteral } from "leaflet";

export function useCurrentLocation() {
  const findMe = useCallback(() => {
    return new Promise<LatLngLiteral>(
      (resolve, reject) => {
        if (!navigator.geolocation) {
          reject(
            new Error("Geolocation is not supported.")
          );

          return;
        }

        navigator.geolocation.getCurrentPosition(
          (position) =>
            resolve({
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            }),
          reject,
          {
            enableHighAccuracy: true,
          }
        );
      }
    );
  }, []);

  return {
    findMe,
  };
}