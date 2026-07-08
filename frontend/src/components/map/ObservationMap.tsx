import {
  MapContainer,
  Marker,
  TileLayer,
  useMap,
  useMapEvents,
} from "react-leaflet";

import {
  Icon,
  type LeafletEvent,
  type LatLngLiteral,
} from "leaflet";

import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

import "leaflet/dist/leaflet.css";

const marker = new Icon({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});

type Props = {
  position: LatLngLiteral;
  onPositionChange: (location: LatLngLiteral) => void;
};

function MapEvents({
  onPositionChange,
}: {
  onPositionChange: (location: LatLngLiteral) => void;
}) {
  useMapEvents({
    click(e) {
      onPositionChange(e.latlng);
    },
  });

  return null;
}

function Recenter({
  position,
}: {
  position: LatLngLiteral;
}) {
  const map = useMap();

  map.setView(position);

  return null;
}

function ObservationMap({
  position,
  onPositionChange,
}: Props) {
  return (
    <MapContainer
      center={position}
      zoom={13}
      className="h-[500px] w-full rounded-xl"
    >
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <Marker
        icon={marker}
        draggable
        position={position}
        eventHandlers={{
          dragend(event: LeafletEvent) {
            onPositionChange(
              event.target.getLatLng()
            );
          },
        }}
      />

      <MapEvents
        onPositionChange={onPositionChange}
      />

      <Recenter position={position} />
    </MapContainer>
  );
}

export default ObservationMap;