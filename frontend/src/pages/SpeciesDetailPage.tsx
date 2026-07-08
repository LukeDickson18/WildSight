import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { getSpeciesById } from "../api/species";

import MainLayout from "../layouts/MainLayout";

import Card from "../components/ui/Card";
import PageHeader from "../components/ui/PageHeader";
import Section from "../components/ui/Section";
import Button from "../components/ui/Button";

import type { Species } from "../types/species";

export default function SpeciesDetailPage() {
    const { id } = useParams();

    const [species, setSpecies] = useState<Species | null>(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (!id) {
            return;
        }

        loadSpecies(id);
    }, [id]);

    async function loadSpecies(id: string) {
        setLoading(true);

        try {
            const response = await getSpeciesById(id);
            setSpecies(response);
        } catch (err) {
            console.error(err);
            setError("Failed to load species.");
        } finally {
            setLoading(false);
        }
    }

    if (loading) {
        return (
            <MainLayout>
                <Card className="p-8 text-center">
                    Loading species...
                </Card>
            </MainLayout>
        );
    }

    if (error || !species) {
        return (
            <MainLayout>
                <Card className="p-8 text-center text-red-600">
                    {error ?? "Species not found."}
                </Card>
            </MainLayout>
        );
    }

    return (
        <MainLayout>
            <Section>
                <Link to="/species">
                    <Button>
                        ← Back to Species
                    </Button>
                </Link>
            </Section>

            <PageHeader
                title={species.common_name}
                description={species.scientific_name}
            />

            <Section>
                <Card className="overflow-hidden">

                    {species.image_url ? (
                        <div className="bg-slate-100 p-8">
                            <div className="mx-auto max-w-4xl overflow-hidden rounded-2xl border-2 border-slate-200 bg-white shadow-xl">
                                <img
                                    src={species.image_url}
                                    alt={species.common_name}
                                    className="max-h-[700px] w-full object-contain"
                                />
                            </div>
                        </div>
                    ) : (
                        <div className="flex h-[500px] items-center justify-center bg-slate-100 text-8xl">
                            🐦
                        </div>
                    )}

                    <div className="space-y-6 p-8">

                        <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

                            <div>
                                <p className="text-sm text-slate-500">
                                    Common Name
                                </p>

                                <p className="text-lg font-semibold">
                                    {species.common_name}
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-500">
                                    Scientific Name
                                </p>

                                <p className="text-lg italic">
                                    {species.scientific_name}
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-500">
                                    Family
                                </p>

                                <p>
                                    {species.family.scientific_name}
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-500">
                                    Order
                                </p>

                                <p>
                                    {species.family.order.name}
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-500">
                                    Wildlife Group
                                </p>

                                <p>
                                    {species.wildlife_group}
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-500">
                                    eBird Code
                                </p>

                                <p>
                                    {species.ebird_code}
                                </p>
                            </div>

                        </div>

                        {(species.image_attribution || species.image_license) && (
                            <div className="border-t pt-6 text-sm text-slate-500">

                                <p className="font-medium">
                                    Photo Credit
                                </p>

                                <p>
                                    {species.image_attribution}
                                </p>

                                <p>
                                    {species.image_license}
                                    {" • "}
                                    {species.image_source}
                                </p>

                            </div>
                        )}

                    </div>

                </Card>
            </Section>
        </MainLayout>
    );
}