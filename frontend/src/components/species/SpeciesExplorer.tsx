import { useEffect, useState } from "react";

import { getSpeciesExplorer } from "../../api/speciesExplorer";

import SpeciesGroup from "../species/speciesGroup";

import type {
    ExplorerGroup,
    ExplorerSpecies,
} from "../../types/speciesExplorer";

interface Props {
    onSpeciesClick: (species: ExplorerSpecies) => void;
}

export default function SpeciesExplorer({
    onSpeciesClick,
}: Props) {

    const [groups, setGroups] = useState<ExplorerGroup[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function loadSpecies() {

            try {

                const response =
                    await getSpeciesExplorer();

                setGroups(response.groups);

            } catch (err) {

                setError(
                    err instanceof Error
                        ? err.message
                        : "Unknown error",
                );

            } finally {

                setLoading(false);

            }

        }

        loadSpecies();

    }, []);

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

    return (
        <div className="space-y-12">

            {groups.map((group) => (
                <SpeciesGroup
                    key={group.scientific_name}
                    group={group}
                    onSpeciesClick={onSpeciesClick}
                />
            ))}

        </div>
    );
}