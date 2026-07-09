import SpeciesGroup from "../species/speciesGroup";

import type {
    SpeciesExplorerSpecies,
} from "../../types/species";

interface Props {
    species: SpeciesExplorerSpecies[];
    loading: boolean;
    error: string;

    onSpeciesClick: (
        species: SpeciesExplorerSpecies,
    ) => void;
}

export default function SpeciesExplorer({
    species,
    loading,
    error,
    onSpeciesClick,
}: Props) {
    if (loading) {
        return (
            <p className="py-8 text-center">
                Loading species...
            </p>
        );
    }

    if (error) {
        return (
            <p className="py-8 text-center text-red-600">
                {error}
            </p>
        );
    }

    const groups = species.reduce<
        Record<string, SpeciesExplorerSpecies[]>
    >((accumulator, current) => {
        const order =
            current.order_common_name ?? "Unknown";

        if (!accumulator[order]) {
            accumulator[order] = [];
        }

        accumulator[order].push(current);

        return accumulator;
    }, {});

    return (
        <div className="space-y-12">
            {Object.entries(groups).map(
                ([orderName, species]) => (
                    <SpeciesGroup
                        key={orderName}
                        orderName={orderName}
                        species={species}
                        onSpeciesClick={
                            onSpeciesClick
                        }
                    />
                ),
            )}
        </div>
    );
}