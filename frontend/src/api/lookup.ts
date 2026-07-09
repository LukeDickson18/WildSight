import { request } from "./client";

import type {
    CountryLookup,
    OrderLookup,
    FamilyLookup,
    HotspotLookup,
} from "../types/lookup";

export function getCountries(): Promise<CountryLookup[]> {
    return request("/species/lookup/countries");
}

export function getOrders(): Promise<OrderLookup[]> {
    return request("/species/lookup/orders");
}

export function getFamilies(): Promise<FamilyLookup[]> {
    return request("/species/lookup/families");
}

export function getHotspots(): Promise<HotspotLookup[]> {
    return request("/species/lookup/hotspots");
}