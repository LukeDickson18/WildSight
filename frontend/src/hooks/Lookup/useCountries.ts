import { getCountries } from "../../api/lookup";
import { useLookup } from "./useLookup";

import type { CountryLookup } from "../../types/lookup";

export function useCountries() {
    return useLookup<CountryLookup>({
        queryKey: "countries",
        queryFn: getCountries,
    });
}