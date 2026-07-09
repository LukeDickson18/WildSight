import Card from "../ui/Card";
import SearchInput from "../ui/SearchInput";

type Props = {
  value: string;
  onChange: (value: string) => void;
  onSearch?: () => void;
};

function SpeciesSearchBar({
  value,
  onChange,
  onSearch,
}: Props) {
  return (
    <Card className="mb-10">
      <SearchInput
        value={value}
        placeholder="Search birds..."
        onChange={onChange}
        onSearch={onSearch}
      />
    </Card>
  );
}

export default SpeciesSearchBar;