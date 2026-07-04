import { request } from "./client";
import type {
  Observation,
  ObservationCreate,
  ObservationListResponse,
  ObservationUpdate,
} from "../types/observation";

export function getObservations(
  page = 1,
  pageSize = 50,
  token?: string,
): Promise<ObservationListResponse> {
  return request(
    `/observations?page=${page}&page_size=${pageSize}`,
    {
      token,
    },
  );
}

export function getObservationById(
  id: string,
  token?: string,
): Promise<Observation> {
  return request(`/observations/${id}`, {
    token,
  });
}

export function createObservation(
  observation: ObservationCreate,
  token: string,
): Promise<Observation> {
  return request("/observations", {
    method: "POST",
    token,
    body: JSON.stringify(observation),
  });
}

export function updateObservation(
  id: string,
  observation: ObservationUpdate,
  token: string,
): Promise<Observation> {
  return request(`/observations/${id}`, {
    method: "PUT",
    token,
    body: JSON.stringify(observation),
  });
}

export function deleteObservation(
  id: string,
  token: string,
): Promise<void> {
  return request(`/observations/${id}`, {
    method: "DELETE",
    token,
  });
}