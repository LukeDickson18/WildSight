import Card from "../ui/Card";
import Select from "../ui/Select";
import Switch from "../ui/Switch";

type Props = {
  useMyLocation: boolean;
  radius: string;
  country: string;
  hotspot: string;

  onUseMyLocationChange: (value: boolean) => void;
  onRadiusChange: (value: string) => void;
  onCountryChange: (value: string) => void;
  onHotspotChange: (value: string) => void;
};

const radiusOptions = [
  { value: "10", label: "10 km" },
  { value: "25", label: "25 km" },
  { value: "50", label: "50 km" },
  { value: "100", label: "100 km" },
  { value: "250", label: "250 km" },
];

const countryOptions = [
  { value: "South Africa", label: "South Africa" },
];

const hotspotOptions = [
  { value: "Any", label: "Any Hotspot" },
];

function SpeciesFilters({
  useMyLocation,
  radius,
  country,
  hotspot,
  onUseMyLocationChange,
  onRadiusChange,
  onCountryChange,
  onHotspotChange,
}: Props) {
  return (
    <Card className="mb-8">
      <div className="flex flex-col gap-8">
        <Switch
          label="Use My Location"
          checked={useMyLocation}
          onChange={onUseMyLocationChange}
        />

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          <Select
            id="radius"
            label="Radius"
            value={radius}
            options={radiusOptions}
            onChange={(e) => onRadiusChange(e.target.value)}
          />

          <Select
            id="country"
            label="Country"
            value={country}
            options={countryOptions}
            onChange={(e) => onCountryChange(e.target.value)}
          />

          <Select
            id="hotspot"
            label="Hotspot"
            value={hotspot}
            options={hotspotOptions}
            onChange={(e) => onHotspotChange(e.target.value)}
          />
        </div>
      </div>
    </Card>
  );
}

export default SpeciesFilters;