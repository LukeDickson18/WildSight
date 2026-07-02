import MainLayout from "../layouts/MainLayout";

import HeroSection from "../components/HeroSection";
import RecentSightings from "../components/RecentSightings";
import MapPreview from "../components/MapPreview";

import Section from "../components/ui/Section";
import StatCard from "../components/ui/StatCard";

function HomePage() {
  return (
    <MainLayout>
      <HeroSection />

      <Section title="WildSight at a Glance">
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          <StatCard title="Sightings" value="1,204+" />
          <StatCard title="Species" value="563" />
          <StatCard title="Hotspots" value="27" />
          <StatCard title="Accuracy" value="89%" />
        </div>
      </Section>

      <Section title="Recent Sightings">
        <RecentSightings />
      </Section>

      <Section title="Explore the Map">
        <MapPreview />
      </Section>
    </MainLayout>
  );
}

export default HomePage;