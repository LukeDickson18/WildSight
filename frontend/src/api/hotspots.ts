import { request } from "./client";

import type {
  HotspotListResponse,
  NearbyHotspotListResponse,
} from "../types/hotspots";

export async function getHotspots(
  page = 1,
  pageSize = 50,
): Promise<HotspotListResponse> {
  return request(
    `/hotspots?page=${page}&page_size=${pageSize}`,
  );
}

export async function getNearbyHotspots(
  latitude: number,
  longitude: number,
  radius = 5,
  page = 1,
  pageSize = 20,
): Promise<NearbyHotspotListResponse> {
  return request(
    `/hotspots/nearby?latitude=${latitude}&longitude=${longitude}&radius=${radius}&page=${page}&page_size=${pageSize}`,
  );
}