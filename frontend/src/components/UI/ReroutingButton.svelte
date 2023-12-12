<script>
	// @ts-nocheck
	import { minute, reroutingMode, canReroute, busNetwork } from '../../stores/stores';

	function setRerouting() {
		let temp = $reroutingMode;
		reroutingMode.set(!temp);
		console.log($busNetwork);
	}
</script>

<body class="relative flex justify-end" class:hidden={!$canReroute || $minute === 0}>
	<div class="absolute flex justify-center p-4 mt-16 mr-3 bg-white rounded-lg top-96">
		<div>Rerouting mode</div>
		<!-- Start: TOGGLE -->
		<label class="relative items-center ml-4 cursor-pointer enable-button">
			<input
				type="checkbox"
				value=""
				class="sr-only peer"
				on:change={() => {
					setRerouting();
				}}
			/>
			<div
				class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
			/>
		</label>
		<!-- END: TOGGLE -->
	</div>
</body>
