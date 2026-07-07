import { Search, Plus } from "lucide-react";
import { useNavigate } from "react-router-dom";

import Button from "../ui/Button";

interface ObservationToolbarProps {
  search: string;
  onSearchChange: (value: string) => void;
}

export default function ObservationToolbar({
  search,
  onSearchChange,
}: ObservationToolbarProps) {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
      <div className="relative flex-1 max-w-xl">
        <Search
          className="absolute left-3 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400"
        />

        <input
          type="text"
          value={search}
          onChange={(e) =>
            onSearchChange(e.target.value)
          }
          placeholder="Search observations..."
          className="w-full rounded-lg border border-slate-300 bg-white py-2.5 pl-10 pr-4 shadow-sm transition focus:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
      </div>

      <Button
        onClick={() =>
          navigate("/observations/new")
        }
      >
        <Plus className="mr-2 h-4 w-4" />
        Log Observation
      </Button>
    </div>
  );
}