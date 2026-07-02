import type { ReactNode } from "react";

import Navbar from "../components/Navbar";
import Container from "../components/ui/Container";

type MainLayoutProps = {
  children: ReactNode;
};

function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />

      <Container className="py-10">
        {children}
      </Container>
    </div>
  );
}

export default MainLayout;