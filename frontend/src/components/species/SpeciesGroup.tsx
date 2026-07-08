import SpeciesCard from "../species/speciesCard";

import type {
    ExplorerGroup,
    ExplorerSpecies,
} from "../../types/speciesExplorer";

interface Props {
    group: ExplorerGroup;
    onSpeciesClick: (species: ExplorerSpecies) => void;
}

export default function SpeciesGroup({
    group,
    onSpeciesClick,
}: Props) {
    return (
        <section className="space-y-4">

            <div>
                <h2 className="text-2xl font-bold">
                    {group.name}
                </h2>

                <p className="text-slate-500 italic">
                    {group.scientific_name}
                </p>
            </div>

            <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6">

                {group.species.map((species) => (
                    <SpeciesCard
                        key={species.id}
                        species={species}
                        onClick={onSpeciesClick}
                    />
                ))}

            </div>

        </section>
    );
}