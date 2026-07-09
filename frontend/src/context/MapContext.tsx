import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from "react";

import type { LatLngLiteral } from "leaflet";

type MapContextType = {
  mapLocation: LatLngLiteral;
  setMapLocation: (location: LatLngLiteral) => void;
};

const MapContext = createContext<MapContextType | null>(null);

type MapProviderProps = {
  children: ReactNode;
};

export function MapProvider({ children }: MapProviderProps) {
  const [mapLocation, setMapLocation] = useState<LatLngLiteral>({
    lat: -33.934,
    lng: 18.866,
  });

  return (
    <MapContext.Provider
      value={{
        mapLocation,
        setMapLocation,
      }}
    >
      {children}
    </MapContext.Provider>
  );
}

export function useMap() {
  const context = useContext(MapContext);

  if (!context) {
    throw new Error("useMap must be used inside MapProvider.");
  }

  return context;
}