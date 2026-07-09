import { Search } from "lucide-react";

type SearchInputProps = {
  value: string;
  placeholder?: string;
  onChange: (value: string) => void;
  onSearch?: () => void;
};

function SearchInput({
  value,
  placeholder = "Search...",
  onChange,
  onSearch,
}: SearchInputProps) {
  function handleKeyDown(
    event: React.KeyboardEvent<HTMLInputElement>
  ) {
    if (event.key === "Enter") {
      onSearch?.();
    }
  }

  return (
    <div className="relative">
      <Search
        className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
        size={20}
      />

      <input
        type="text"
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        className="w-full rounded-xl border border-slate-300 bg-white py-3 pl-12 pr-4 outline-none transition focus:border-green-600 focus:ring-2 focus:ring-green-100"
      />
    </div>
  );
}

export default SearchInput;