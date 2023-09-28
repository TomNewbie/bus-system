<script>
	// @ts-nocheck

	import { onDestroy, setContext } from 'svelte';
	import { mapbox, key } from './mapbox.js';

	setContext(key, {
		// @ts-ignore
		getMap: () => map
	});

	// @ts-ignore
	export let lat;
	// @ts-ignore
	export let lon;
	// @ts-ignore
	export let zoom;

	// @ts-ignore
	let container;
	// @ts-ignore
	let map;

	function load() {
		map = new mapbox.Map({
			// @ts-ignore
			container,
			style: 'mapbox://styles/mapbox/streets-v9',
			// @ts-ignore
			center: [lon, lat],
			// @ts-ignore
			zoom
		});
	}

	onDestroy(() => {
		// @ts-ignore
		if (map) map.remove();
	});
</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/mapbox-gl/dist/mapbox-gl.css" on:load={load} />
</svelte:head>

<div class="relative min-h-screen min-w-screen">
	<div bind:this={container} class="map-container">
		{#if map}
			<slot />
		{/if}
	</div>
</div>

<style>
	/* Ensure the map container covers the entire screen */
	.map-container {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
	}
</style>
