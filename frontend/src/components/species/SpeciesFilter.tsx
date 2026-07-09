import Card from "../ui/Card";
import Select from "../ui/Select";
import Switch from "../ui/Switch";

import { radiusOptions } from "../../constants/speciesFilters";

import { useCountries } from "../../hooks/Lookup/useCountries";
import { useHotspots } from "../../hooks/Lookup/useHotspots";

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
  const { data: countries = [] } = useCountries();
  const { data: hotspots = [] } = useHotspots();

  const countryOptions = [
    {
      value: "",
      label: "All Countries",
    },
    ...countries.map((country) => ({
      value: country.id,
      label: country.name,
    })),
  ];

  const hotspotOptions = [
    {
      value: "",
      label: "All Hotspots",
    },
    ...hotspots.map((hotspot) => ({
      value: hotspot.id,
      label: hotspot.name,
    })),
  ];

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
            disabled={!useMyLocation}
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