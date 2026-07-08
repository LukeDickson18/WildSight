import type { Species } from "../types/species";

interface SpeciesTableProps {
    species: Species[];
    onSelect?: (species: Species) => void;
}

export default function SpeciesTable({
    species,
    onSelect,
}: SpeciesTableProps) {
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-slate-200">
                <thead className="bg-slate-50">
                    <tr className="text-left text-sm font-semibold text-slate-700">
                        <th className="px-4 py-3">Photo</th>
                        <th className="px-4 py-3">Common Name</th>
                        <th className="px-4 py-3">Scientific Name</th>
                        <th className="px-4 py-3">Family</th>
                        <th className="px-4 py-3">Order</th>
                    </tr>
                </thead>

                <tbody className="divide-y divide-slate-100">
                    {species.map((bird) => (
                        <tr
                            key={bird.id}
                            onClick={() => onSelect?.(bird)}
                            className="cursor-pointer transition-colors hover:bg-slate-50"
                        >
                            <td className="px-4 py-3">
                                {bird.thumbnail_url ? (
                                    <img
                                        src={bird.thumbnail_url}
                                        alt={bird.common_name}
                                        className="h-14 w-14 rounded-lg border border-slate-200 object-cover transition-transform duration-200 hover:scale-110"
                                    />
                                ) : (
                                    <div className="flex h-14 w-14 items-center justify-center rounded-lg border border-slate-200 bg-slate-100 text-2xl">
                                        🐦
                                    </div>
                                )}
                            </td>

                            <td className="px-4 py-3 font-medium text-slate-900">
                                {bird.common_name}
                            </td>

                            <td className="px-4 py-3 italic text-slate-600">
                                {bird.scientific_name}
                            </td>

                            <td className="px-4 py-3 text-slate-700">
                                {bird.family.scientific_name}
                            </td>

                            <td className="px-4 py-3 text-slate-700">
                                {bird.family.order.name}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}