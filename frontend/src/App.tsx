import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import StatsSection from "./components/StatsSection";
import RecentSightings from "./components/RecentSightings";

function App() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />
      <Hero />
      <StatsSection />
      <RecentSightings />
    </div>
  );
}

export default App;