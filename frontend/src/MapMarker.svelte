<script>
  import { getContext } from "svelte";
  import { mapbox, key } from "./mapbox.js";

  const { getMap } = getContext(key);
  const map = getMap();

  export let lat;
  export let lon;
  export let label;

  const markerElement = document.createElement("div");
  markerElement.className = "custom-marker";
  markerElement.style.backgroundColor = "blue"; // Customize the color of the circle
  markerElement.style.borderRadius = "50%"; // Make it circular
  markerElement.style.width = "5px"; // Customize the size of the circle
  markerElement.style.height = "5px";
  markerElement.style.transform = "translate(-50%, -50%)"; // Center the marker

  const popup = new mapbox.Popup({ offset: 25 }).setText(label);

  const customMarker = new mapbox.Marker({
    element: markerElement,
  })
    .setLngLat([lon, lat])
    .setPopup(popup)
    .addTo(map);
</script>
