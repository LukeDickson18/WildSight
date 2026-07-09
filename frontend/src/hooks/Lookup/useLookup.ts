import { useQuery } from "@tanstack/react-query";

type UseLookupOptions<T> = {
    queryKey: string;
    queryFn: () => Promise<T[]>;
};

export function useLookup<T>({
    queryKey,
    queryFn,
}: UseLookupOptions<T>) {
    return useQuery({
        queryKey: [queryKey],
        queryFn,
        staleTime: 1000 * 60 * 60,
    });
}