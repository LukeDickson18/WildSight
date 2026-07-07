import { request } from "./client";

import type {
  Observation,
  ObservationCreate,
  ObservationListResponse,
  ObservationQueryParams,
  ObservationUpdate,
} from "../types/observation";

export async function getObservations({
  page = 1,
  pageSize = 25,
  search,
  speciesId,
  startDate,
  endDate,
  sort = "newest",
  token,
}: ObservationQueryParams): Promise<ObservationListResponse> {
  const params = new URLSearchParams();

  params.set("page", page.toString());
  params.set("page_size", pageSize.toString());

  if (search) {
    params.set("search", search);
  }

  if (speciesId) {
    params.set("species_id", speciesId);
  }

  if (startDate) {
    params.set("start_date", startDate);
  }

  if (endDate) {
    params.set("end_date", endDate);
  }

  params.set("sort", sort);

  return request(
    `/observations?${params.toString()}`,
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