<script>
	// @ts-nocheck

	// @ts-ignore
	export let bus_id;
	export let bus_start;
	export let bus_end;
	export let handleClick;
	$: busClass = `bus-${bus_id}`;
</script>

<body>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div
		class="flex items-center h-full pt-3 border-t-2 border-solid gap-x-1 justify-left {busClass}"
		on:click={() => handleClick(bus_id)}
		style="cursor: pointer;"
	>
		<div
			class="ml-6 mr-1 bg-[#DBF6D0] text-[#3A6727] px-2 py-1 font-semibold rounded-md border-solid border-2 border-white text-sm"
		>
			{bus_id}
		</div>

		<div class="mr-1 text-base text-black font-regular">{bus_start} → {bus_end}</div>
	</div>
</body>
