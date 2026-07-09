import { getFamilies } from "../../api/lookup";
import { useLookup } from "./useLookup";

import type { FamilyLookup } from "../../types/lookup";

export function useFamilies() {
    return useLookup<FamilyLookup>({
        queryKey: "families",
        queryFn: getFamilies,
    });
}