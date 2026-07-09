import { useState } from "react";
import { ChevronRight, ImageOff } from "lucide-react";

import Card from "../ui/Card";

import type { SpeciesExplorerSpecies } from "../../types/species";

type Props = {
    species: SpeciesExplorerSpecies;
    onClick: () => void;
};

function SpeciesCard({
    species,
    onClick,
}: Props) {
    const [imageError, setImageError] = useState(false);

    const image =
        species.thumbnail_url ??
        species.image_url;

    return (
        <Card
            className="
                cursor-pointer
                overflow-hidden
                p-0
                transition-all
                duration-300
                hover:-translate-y-1
                hover:shadow-xl
            "
        >
            <button
                onClick={onClick}
                className="block h-full w-full text-left"
            >
                <div className="aspect-[4/3] bg-slate-100">
                    {!image || imageError ? (
                        <div className="flex h-full items-center justify-center text-slate-400">
                            <ImageOff size={40} />
                        </div>
                    ) : (
                        <img
                            src={image}
                            alt={species.common_name}
                            className="
                                h-full
                                w-full
                                object-cover
                                transition-transform
                                duration-500
                                group-hover:scale-105
                            "
                            onError={() =>
                                setImageError(true)
                            }
                        />
                    )}
                </div>

                <div className="space-y-3 p-5">
                    <div>
                        <h3 className="line-clamp-2 text-lg font-semibold text-slate-900">
                            {species.common_name}
                        </h3>

                        <p className="mt-1 italic text-slate-500">
                            {species.scientific_name}
                        </p>
                    </div>

                    {species.family_common_name && (
                        <span className="inline-flex rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
                            {species.family_common_name}
                        </span>
                    )}

                    <div className="flex items-center justify-between pt-2 text-sm font-medium text-green-700">
                        <span>View details</span>

                        <ChevronRight size={18} />
                    </div>
                </div>
            </button>
        </Card>
    );
}

export default SpeciesCard;