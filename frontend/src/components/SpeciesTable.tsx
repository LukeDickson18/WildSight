import type { Species } from "../types/species";

interface SpeciesTableProps {
    species: Species[];
}

export default function SpeciesTable({
    species,
}: SpeciesTableProps) {
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
                <thead>
                    <tr className="text-left">
                        <th className="px-4 py-2">Common Name</th>
                        <th className="px-4 py-2">Scientific Name</th>
                        <th className="px-4 py-2">Family</th>
                        <th className="px-4 py-2">Order</th>
                    </tr>
                </thead>

                <tbody>
                    {species.map((bird) => (
                        <tr
                            key={bird.id}
                            className="border-t"
                        >
                            <td className="px-4 py-2">
                                {bird.common_name}
                            </td>

                            <td className="px-4 py-2 italic">
                                {bird.scientific_name}
                            </td>

                            <td className="px-4 py-2">
                                {bird.family.scientific_name}
                            </td>

                            <td className="px-4 py-2">
                                {bird.family.order.name}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}