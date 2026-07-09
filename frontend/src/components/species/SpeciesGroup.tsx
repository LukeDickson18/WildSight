import SpeciesCard from "../species/speciesCard";

import type { SpeciesExplorerSpecies } from "../../types/species";

type Props = {
    orderName: string;
    species: SpeciesExplorerSpecies[];
    onSpeciesClick: (
        species: SpeciesExplorerSpecies,
    ) => void;
};

function SpeciesGroup({
    orderName,
    species,
    onSpeciesClick,
}: Props) {
    return (
        <section className="mb-16">
            <header className="mb-8 border-b border-slate-200 pb-5">
                <div className="flex flex-col gap-2 md:flex-row md:items-end md:justify-between">
                    <div>
                        <h2 className="text-3xl font-bold text-slate-900">
                            {orderName}
                        </h2>
                    </div>

                    <span className="text-sm font-medium text-slate-500">
                        {species.length} species
                    </span>
                </div>
            </header>

            <div
                className="
                    grid
                    grid-cols-1
                    gap-6
                    sm:grid-cols-2
                    lg:grid-cols-3
                    xl:grid-cols-4
                "
            >
                {species.map((bird) => (
                    <SpeciesCard
                        key={bird.id}
                        species={bird}
                        onClick={() =>
                            onSpeciesClick(bird)
                        }
                    />
                ))}
            </div>
        </section>
    );
}

export default SpeciesGroup;