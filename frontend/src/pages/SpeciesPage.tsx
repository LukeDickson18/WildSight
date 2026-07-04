import { useEffect, useState } from "react";

import {
  getSpecies,
  searchSpecies,
} from "../api/species";

import SpeciesTable from "../components/SpeciesTable";

import Card from "../components/ui/Card";
import Container from "../components/ui/Container";
import Input from "../components/ui/Input";
import PageHeader from "../components/ui/PageHeader";
import Section from "../components/ui/Section";
import StatCard from "../components/ui/StatCard";
import Button from "../components/ui/Button";

import type {
  Species,
  SpeciesListResponse,
} from "../types/species";

export default function SpeciesPage() {
  const [species, setSpecies] = useState<Species[]>([]);
  const [search, setSearch] = useState("");

  const [page, setPage] = useState(1);

  const [totalSpecies, setTotalSpecies] = useState(0);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const timeout = setTimeout(() => {
      loadSpecies();
    }, 300);

    return () => clearTimeout(timeout);
  }, [search, page]);

  async function loadSpecies() {
    setLoading(true);
    setError(null);

    try {
      let response: SpeciesListResponse;

      if (search.trim() === "") {
        response = await getSpecies(page);
      } else {
        response = await searchSpecies(
          search,
          page,
        );
      }

      setSpecies(response.items);
      setTotalSpecies(response.total);
    } catch (err) {
      console.error(err);
      setError("Failed to load species.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Container>
      <PageHeader
        title="Species Explorer"
        description="Browse and search all species available in WildSight."
      />

      <Section>
        <Input
          placeholder="Search common or scientific name..."
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            setPage(1);
          }}
        />
      </Section>

      <Section>
        <StatCard
          title="Total Species"
          value={totalSpecies}
        />
      </Section>

      {loading && (
        <Card className="p-8 text-center">
          Loading species...
        </Card>
      )}

      {error && (
        <Card className="p-8 text-center text-red-600">
          {error}
        </Card>
      )}

      {!loading && !error && (
        <Section>
          <Card>
            <SpeciesTable species={species} />
          </Card>

          <div className="mt-6 flex items-center justify-between">
            <Button
              disabled={page === 1}
              onClick={() =>
                setPage((p) => p - 1)
              }
            >
              Previous
            </Button>

            <span className="text-sm text-slate-600">
              Page {page}
            </span>

            <Button
              disabled={species.length < 50}
              onClick={() =>
                setPage((p) => p + 1)
              }
            >
              Next
            </Button>
          </div>
        </Section>
      )}
    </Container>
  );
}