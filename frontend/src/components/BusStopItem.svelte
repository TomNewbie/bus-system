<script>
	// @ts-nocheck

	// @ts-ignore
	export let stop_id;
	export let stop_name;
</script>

<body>
	<div class="flex items-center h-full pt-3 gap-x-1 justify-left">
		<div
			class=" mx-6 bg-[#F7DFDE] text-[#F01B48] px-3 py-1 font-semibold rounded-md border-solid border-2 border-white text-base"
		>
			{stop_id}
		</div>

		<div class="text-base text-black font-regular">{stop_name}</div>
	</div>
</body>
