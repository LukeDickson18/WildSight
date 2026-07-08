import { BrowserRouter, Routes, Route } from "react-router-dom";

import ProtectedRoute from "./ProtectedRoute";

import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import DashboardPage from "../pages/DashboardPage";
import SpeciesPage from "../pages/SpeciesPage";
import SpeciesDetailPage from "../pages/SpeciesDetailPage";
import NotFoundPage from "../pages/NotFoundPage";
import ObservationsPage from "../pages/ObservationPage";
import NewObservationPage from "../pages/NewObservationPage";
import MapPage from "../pages/MapPage";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/login" element={<LoginPage />} />

        <Route path="/register" element={<RegisterPage />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <DashboardPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/species"
          element={
            <ProtectedRoute>
              <SpeciesPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/species/:id"
          element={
            <ProtectedRoute>
              <SpeciesDetailPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/observations"
          element={
            <ProtectedRoute>
              <ObservationsPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/observations/new"
          element={
            <ProtectedRoute>
              <NewObservationPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/map"
          element={
            <ProtectedRoute>
              <MapPage />
            </ProtectedRoute>
          }
        />
        {/* Fallback route */}
        <Route path="*" element={<NotFoundPage />} />

      </Routes>
    </BrowserRouter>
  );
}

export default AppRouter;