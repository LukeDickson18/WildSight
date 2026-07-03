import { NavLink } from "react-router-dom";

import { useAuth } from "../auth/useAuth";
import Button from "./ui/Button";
import Container from "./ui/Container";

function Navbar() {
  const { isAuthenticated, logout, user } = useAuth();

  const navLinkClasses = ({ isActive }: { isActive: boolean }) =>
    isActive
      ? "font-semibold text-green-700"
      : "font-medium text-slate-600 transition hover:text-green-700";

  return (
    <nav className="border-b bg-white shadow-sm">
      <Container className="flex items-center justify-between py-5">
        <NavLink
          to="/"
          className="text-2xl font-bold text-green-700"
        >
          🌿 WildSight
        </NavLink>

        <div className="flex items-center gap-6">
          <NavLink to="/" className={navLinkClasses}>
            Home
          </NavLink>

          <NavLink to="/dashboard" className={navLinkClasses}>
            Dashboard
          </NavLink>

          {isAuthenticated ? (
            <>
              <span className="font-medium text-slate-600">
                {user?.username}
              </span>

              <Button variant="secondary" onClick={logout}>
                Logout
              </Button>
            </>
          ) : (
            <>
              <NavLink to="/login">
                <Button variant="secondary">
                  Login
                </Button>
              </NavLink>

              <NavLink to="/register">
                <Button>
                  Sign Up
                </Button>
              </NavLink>
            </>
          )}
        </div>
      </Container>
    </nav>
  );
}

export default Navbar;
