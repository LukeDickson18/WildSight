import { useCallback, useEffect, useMemo, useState, type ReactNode } from "react";

import {
  getCurrentUser,
  loginUser,
  registerUser,
  type LoginRequest,
  type RegisterRequest,
  type User,
} from "../api/auth";
import { AuthContext, type AuthContextValue } from "./authState";

const AUTH_TOKEN_KEY = "wildsight_access_token";

type AuthProviderProps = {
  children: ReactNode;
};

export function AuthProvider({ children }: AuthProviderProps) {
  const [token, setToken] = useState<string | null>(() =>
    localStorage.getItem(AUTH_TOKEN_KEY),
  );
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const logout = useCallback(() => {
    localStorage.removeItem(AUTH_TOKEN_KEY);
    setToken(null);
    setUser(null);
  }, []);

  useEffect(() => {
    let isMounted = true;

    async function loadUser() {
      if (token === null) {
        setIsLoading(false);
        return;
      }

      try {
        const currentUser = await getCurrentUser(token);
        if (isMounted) {
          setUser(currentUser);
        }
      } catch {
        if (isMounted) {
          logout();
        }
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    }

    loadUser();

    return () => {
      isMounted = false;
    };
  }, [logout, token]);

  const login = useCallback(async (payload: LoginRequest) => {
    const response = await loginUser(payload);
    localStorage.setItem(AUTH_TOKEN_KEY, response.access_token);
    setToken(response.access_token);
    setUser(await getCurrentUser(response.access_token));
  }, []);

  const register = useCallback(async (payload: RegisterRequest) => {
    await registerUser(payload);
    const response = await loginUser({
      email: payload.email,
      password: payload.password,
    });
    localStorage.setItem(AUTH_TOKEN_KEY, response.access_token);
    setToken(response.access_token);
    setUser(await getCurrentUser(response.access_token));
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      token,
      isAuthenticated: user !== null && token !== null,
      isLoading,
      login,
      register,
      logout,
    }),
    [isLoading, login, logout, register, token, user],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
