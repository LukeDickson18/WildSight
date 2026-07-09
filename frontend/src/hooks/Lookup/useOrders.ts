import { getOrders } from "../../api/lookup";
import { useLookup } from "./useLookup";

import type { OrderLookup } from "../../types/lookup";

export function useOrders() {
    return useLookup<OrderLookup>({
        queryKey: "orders",
        queryFn: getOrders,
    });
}