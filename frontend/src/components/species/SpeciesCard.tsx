import type { ExplorerSpecies } from "../../types/speciesExplorer";

interface Props {
    species: ExplorerSpecies;
    onClick: (species: ExplorerSpecies) => void;
}

export default function SpeciesCard({
    species,
    onClick,
}: Props) {
    return (
        <button
            onClick={() => onClick(species)}
            className="overflow-hidden rounded-xl border bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-lg"
        >
            <div className="aspect-square bg-slate-100">
                {species.thumbnail_url ? (
                    <img
                        src={species.thumbnail_url}
                        alt={species.common_name}
                        className="h-full w-full object-cover"
                    />
                ) : (
                    <div className="flex h-full items-center justify-center text-5xl">
                        🐦
                    </div>
                )}
            </div>

            <div className="p-3">
                <h3 className="text-center text-sm font-medium">
                    {species.common_name}
                </h3>
            </div>
        </button>
    );
}