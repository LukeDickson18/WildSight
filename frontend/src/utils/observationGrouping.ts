import type { Observation } from "../types/observation";

export interface ObservationGroup {
  title: string;
  observations: Observation[];
}

export function groupObservations(
  observations: Observation[],
): ObservationGroup[] {
  const today = new Date();

  const yesterday = new Date();
  yesterday.setDate(today.getDate() - 1);

  const groups = new Map<
    string,
    Observation[]
  >();

  observations.forEach((observation) => {
    const date = new Date(
      observation.observation_datetime,
    );

    let title: string;

    if (
      date.toDateString() ===
      today.toDateString()
    ) {
      title = "Today";
    } else if (
      date.toDateString() ===
      yesterday.toDateString()
    ) {
      title = "Yesterday";
    } else {
      title = date.toLocaleDateString(
        undefined,
        {
          month: "long",
          year: "numeric",
        },
      );
    }

    if (!groups.has(title)) {
      groups.set(title, []);
    }

    groups.get(title)!.push(observation);
  });

  return Array.from(groups.entries()).map(
    ([title, observations]) => ({
      title,
      observations,
    }),
  );
}