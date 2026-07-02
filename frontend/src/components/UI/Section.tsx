import type { ReactNode } from "react";

type SectionProps = {
  title: string;
  children: ReactNode;
};

function Section({
  title,
  children,
}: SectionProps) {
  return (
    <section className="mb-16">
      <h2 className="mb-6 text-2xl font-bold">
        {title}
      </h2>

      {children}
    </section>
  );
}

export default Section;