<script>
  import Map from "./Map.svelte";
  import MapMarker from "./MapMarker.svelte";
  import { onMount } from "svelte";

  let dataArray = []; // Initialize an empty array to store the parsed data

  onMount(async () => {
    try {
      const response = await fetch("data.json"); // Replace with the actual path to your JSON file
      if (response.ok) {
        dataArray = await response.json();
      } else {
        throw new Error("Failed to fetch data");
      }
    } catch (error) {
      console.error("Error loading JSON data:", error);
    }
  });
</script>

<!-- ParentComponent.svelte -->

<body>
  <Map lat={21.48} lon={-157.966} zoom={10} {dataArray}>
    {#each dataArray as data}
      <MapMarker
        lat={data.stop_lat}
        lon={data.stop_lon}
        label={data.stop_name}
      />
    {/each}
    <div class="floating-button">
      <div class="vertical-display">
        <input placeholder="Search bus service or bus stop" />
        <p>Cancel</p>
      </div>
    </div>
  </Map>
</body>

<style>
  /* Style for the container */
  .floating-button {
    position: fixed; /* Fixed position to keep it visible while scrolling */
    bottom: 0; /* Adjust the distance from the bottom as needed */
    right: 0; /* Adjust the distance from the right as needed */
    z-index: 1000; /* Adjust the z-index to ensure it's above other elements */
    background-color: white;
    width: 25%;
  }

  .vertical-display {
    display: flex;
    justify-content: space-between;
  }

  .vertical-display input {
    width: 80%;
    margin: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .vertical-display p {
    padding: 5px;
    margin-right: 5px;
  }
</style>
