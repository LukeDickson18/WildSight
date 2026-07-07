import {request} from "./client";

import type { DashboardResponse } from "../types/dashboard";

export async function getDashboard(
  token?: string |null,
): Promise<DashboardResponse> {
  return request(
    "/dashboard",
    {
      token,
    }
  );
}