import Card from "../ui/Card";
import Select from "../ui/Select";
import Switch from "../ui/Switch";

import { radiusOptions } from "../../constants/speciesFilters";

import { useCountries } from "../../hooks/Lookup/useCountries";
import { useFamilies } from "../../hooks/Lookup/useFamilies";
import { useHotspots } from "../../hooks/Lookup/useHotspots";
import { useOrders } from "../../hooks/Lookup/useOrders";

type Props = {
  useMyLocation: boolean;
  radius: string;

  country: string;
  order: string;
  family: string;
  hotspot: string;

  onUseMyLocationChange: (value: boolean) => void;
  onRadiusChange: (value: string) => void;

  onCountryChange: (value: string) => void;
  onOrderChange: (value: string) => void;
  onFamilyChange: (value: string) => void;
  onHotspotChange: (value: string) => void;
};

function SpeciesFilters({
  useMyLocation,
  radius,

  country,
  order,
  family,
  hotspot,

  onUseMyLocationChange,
  onRadiusChange,

  onCountryChange,
  onOrderChange,
  onFamilyChange,
  onHotspotChange,
}: Props) {
  const { data: countries = [] } = useCountries();
  const { data: orders = [] } = useOrders();
  const { data: families = [] } = useFamilies();
  const { data: hotspots = [] } = useHotspots();

  const countryOptions = [
    { value: "", label: "All Countries" },
    ...countries.map((country) => ({
      value: country.id,
      label: country.name,
    })),
  ];

  const orderOptions = [
    { value: "", label: "All Orders" },
    ...orders.map((order) => ({
      value: order.id,
      label: order.common_name ?? order.name,
    })),
  ];

  const familyOptions = [
    { value: "", label: "All Families" },
    ...families.map((family) => ({
      value: family.id,
      label: family.common_name,
    })),
  ];

  const hotspotOptions = [
    { value: "", label: "All Hotspots" },
    ...hotspots.map((hotspot) => ({
      value: hotspot.id,
      label: hotspot.name,
    })),
  ];

  return (
    <Card className="mb-8 p-8">
      <div className="space-y-10">
        {/* Taxonomy */}

        <section>
          <h2 className="mb-1 text-lg font-semibold text-slate-900">
            Taxonomy
          </h2>

          <p className="mb-5 text-sm text-slate-500">
            Narrow species by their biological classification.
          </p>

          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            <Select
              id="order"
              label="Order"
              value={order}
              options={orderOptions}
              onChange={(e) =>
                onOrderChange(e.target.value)
              }
            />

            <Select
              id="family"
              label="Family"
              value={family}
              options={familyOptions}
              onChange={(e) =>
                onFamilyChange(e.target.value)
              }
            />
          </div>
        </section>

        <hr />

        {/* Location */}

        <section>
          <h2 className="mb-1 text-lg font-semibold text-slate-900">
            Location
          </h2>

          <p className="mb-5 text-sm text-slate-500">
            Restrict results to a country, hotspot or
            your current location.
          </p>

          <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
            <Select
              id="country"
              label="Country"
              value={country}
              options={countryOptions}
              onChange={(e) =>
                onCountryChange(e.target.value)
              }
            />

            <Select
              id="hotspot"
              label="Hotspot"
              value={hotspot}
              options={hotspotOptions}
              onChange={(e) =>
                onHotspotChange(e.target.value)
              }
            />
          </div>

          <div className="mt-8 flex flex-col gap-6 rounded-xl bg-slate-50 p-5">
            <Switch
              label="Use My Location"
              checked={useMyLocation}
              onChange={onUseMyLocationChange}
            />

            <Select
              id="radius"
              label="Search Radius"
              value={radius}
              options={radiusOptions}
              disabled={!useMyLocation}
              onChange={(e) =>
                onRadiusChange(e.target.value)
              }
            />
          </div>
        </section>
      </div>
    </Card>
  );
}

export default SpeciesFilters;