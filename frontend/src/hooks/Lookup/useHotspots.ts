import { getHotspots } from "../../api/lookup";
import { useLookup } from "./useLookup";

import type { HotspotLookup } from "../../types/lookup";

export function useHotspots() {
    return useLookup<HotspotLookup>({
        queryKey: "hotspots",
        queryFn: getHotspots,
    });
}