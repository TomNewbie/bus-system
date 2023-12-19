<script>
	// @ts-nocheck
	import {
		reroutingMode,
		start_stop_lon_lat,
		end_stop_lon_lat,
		rerouteIndex
	} from '../../stores/stores';
	export let stop_id;
	export let stop_name;
	export let is_last_stop = false;
	export let start_stop;
	export let end_stop;
	export let index;
	function updateStop() {
		start_stop_lon_lat.set(start_stop);
		end_stop_lon_lat.set(end_stop);
		rerouteIndex.set(index);
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="relative flex pb-10 h-fit">
	<!-- Line -->
	{#if !is_last_stop}
		<div class="absolute inset-0 flex items-center justify-center w-10 h-full bar">
			<div class="w-1 h-full bg-[#F01B48] pointer-events-none" />
		</div>
		{#if $reroutingMode}
			<div class="absolute bottom-0 h-2/5 left-2">
				<img
					src="./trash-can.svg"
					alt="bus-stop"
					class="w-6 h-6"
					style="cursor: pointer;"
					on:click={() => updateStop()}
				/>
			</div>
		{/if}
	{/if}
	<div
		class="relative z-10 inline-flex items-center justify-center flex-shrink-0 w-10 h-10 text-white bg-[#F7DFDE] rounded-full"
	>
		<img src="./busstop.svg" alt="bus-stop" class="w-6 h-6" />
	</div>

	<div class="flex-grow pl-4">
		<div class=" text-[#F01B48] font-semibold text-base">
			{stop_id}
		</div>
		<div class="text-base text-black font-regular">
			{stop_name}
		</div>
	</div>
</div>
