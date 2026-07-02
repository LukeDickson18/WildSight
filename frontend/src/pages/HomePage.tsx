import Hero from "../components/Hero";
import RecentSightings from "../components/RecentSightings";
import StatsSection from "../components/StatsSection";

function HomePage() {
  return (
    <>
      <Hero />
      <StatsSection />
      <RecentSightings />
    </>
  );
}

export default HomePage;