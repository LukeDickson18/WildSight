import { FormEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import { useAuth } from "../auth/useAuth";

import { createObservation } from "../api/observation";
import { searchSpecies } from "../api/species";

import type { Species } from "../types/species";

import Button from "../components/ui/Button";
import Card from "../components/ui/Card";
import Input from "../components/ui/Input";
import PageHeader from "../components/ui/PageHeader";

export default function NewObservationPage() {
  const navigate = useNavigate();
  const { token } = useAuth();

  const [speciesQuery, setSpeciesQuery] = useState("");
  const [speciesResults, setSpeciesResults] = useState<Species[]>([]);
  const [selectedSpecies, setSelectedSpecies] =
    useState<Species | null>(null);

  const [observationDate, setObservationDate] = useState(
    new Date().toISOString().slice(0, 16),
  );

  const [count, setCount] = useState(1);
  const [notes, setNotes] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const timeout = setTimeout(async () => {
      if (speciesQuery.trim().length < 2) {
        setSpeciesResults([]);
        return;
      }

      try {
        const response = await searchSpecies(speciesQuery);
        setSpeciesResults(response.items);
      } catch (err) {
        console.error(err);
      }
    }, 300);

    return () => clearTimeout(timeout);
  }, [speciesQuery]);

  async function handleSubmit(
    e: FormEvent<HTMLFormElement>,
  ) {
    e.preventDefault();

    if (!selectedSpecies) {
      setError("Please select a species.");
      return;
    }

    if (!token) {
      setError("You must be logged in.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      await createObservation(
        {
          species_id: selectedSpecies.id,
          latitude: -33.986,
          longitude: 18.511,
          observation_datetime: new Date(
            observationDate,
          ).toISOString(),
          count,
          notes: notes || null,
        },
        token,
      );

      navigate("/observations");
    } catch (err) {
      console.error(err);
      setError("Failed to create observation.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <MainLayout>
      <div className="mx-auto max-w-3xl space-y-8">
        <PageHeader
          title="Log Observation"
          description="Record a new wildlife observation."
        />

        <Card className="p-8">
          <form
            onSubmit={handleSubmit}
            className="space-y-6"
          >
            <div>
              <label className="mb-2 block font-medium">
                Species
              </label>

              <Input
                placeholder="Search species..."
                value={speciesQuery}
                onChange={(e) => {
                  setSpeciesQuery(e.target.value);
                  setSelectedSpecies(null);
                }}
              />

              {speciesResults.length > 0 &&
                !selectedSpecies && (
                  <div className="mt-2 max-h-60 overflow-y-auto rounded-lg border bg-white">
                    {speciesResults.map((species) => (
                      <button
                        key={species.id}
                        type="button"
                        className="block w-full border-b px-4 py-3 text-left hover:bg-green-50"
                        onClick={() => {
                          setSelectedSpecies(species);
                          setSpeciesQuery(
                            species.common_name,
                          );
                          setSpeciesResults([]);
                        }}
                      >
                        <div className="font-medium">
                          {species.common_name}
                        </div>

                        <div className="text-sm italic text-slate-500">
                          {species.scientific_name}
                        </div>
                      </button>
                    ))}
                  </div>
                )}

              {selectedSpecies && (
                <p className="mt-2 text-green-700">
                  Selected:{" "}
                  <strong>
                    {selectedSpecies.common_name}
                  </strong>
                </p>
              )}
            </div>

            <Input
              label="Observation Date"
              type="datetime-local"
              value={observationDate}
              onChange={(e) =>
                setObservationDate(
                  e.target.value,
                )
              }
            />

            <Input
              label="Count"
              type="number"
              min={1}
              value={count}
              onChange={(e) =>
                setCount(Number(e.target.value))
              }
            />

            <div>
              <label className="mb-2 block font-medium">
                Notes
              </label>

              <textarea
                rows={5}
                className="w-full rounded-lg border border-slate-300 p-3"
                value={notes}
                onChange={(e) =>
                  setNotes(e.target.value)
                }
              />
            </div>

            {error && (
              <div className="rounded-lg bg-red-100 p-4 text-red-700">
                {error}
              </div>
            )}

            <div className="flex gap-4">
              <Button
                type="submit"
                disabled={loading}
              >
                {loading
                  ? "Saving..."
                  : "Save Observation"}
              </Button>

              <Button
                type="button"
                variant="secondary"
                onClick={() =>
                  navigate("/observations")
                }
              >
                Cancel
              </Button>
            </div>
          </form>
        </Card>
      </div>
    </MainLayout>
  );
}