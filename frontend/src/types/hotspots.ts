export interface Hotspot {
  id: string;
  ebird_id: string;
  name: string;
  source: string;

  latitude: number;
  longitude: number;
}

export interface NearbyHotspot extends Hotspot {
  distance_km: number;
}

export interface HotspotListResponse {
  items: Hotspot[];
  total: number;
  page: number;
  page_size: number;
}

export interface NearbyHotspotListResponse {
  items: NearbyHotspot[];
  total: number;
  page: number;
  page_size: number;
}