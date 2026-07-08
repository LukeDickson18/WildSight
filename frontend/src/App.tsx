import AppRouter from "./routes/AppRouter";
import { AuthProvider } from "./auth/AuthProvider";
import { MapProvider } from "./context/MapContext";

function App() {
  return (
    <MapProvider>
      <AuthProvider>
        <AppRouter />
      </AuthProvider>
    </MapProvider>
  );
}

export default App;