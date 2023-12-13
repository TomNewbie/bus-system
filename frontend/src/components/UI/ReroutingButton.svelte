<script>
	// @ts-nocheck
	import { minute, reroutingMode, canReroute, busNetwork } from '../../stores/stores';
	import html2canvas from 'html2canvas';

	function setRerouting() {
		let temp = $reroutingMode;
		reroutingMode.set(!temp);
		console.log($busNetwork);
	}

	function takeScreenshot() {
		const fullScreen = document.documentElement;

		html2canvas(fullScreen).then((canvas) => {
			const imgData = canvas.toDataURL('image/png');

			// Create a link element to download the image
			const link = document.createElement('a');
			link.href = imgData;
			link.download = 'newRoute.png';
			link.click();
		});
	}
</script>

<body class="relative flex justify-end" class:hidden={!$canReroute || $minute === 0}>
	<div class="absolute flex justify-center p-4 mt-16 mr-3 bg-white rounded-lg top-96">
		<div class="mt-3">Rerouting mode</div>
		<!-- Start: TOGGLE -->
		<label class="relative items-center mt-3 ml-4 cursor-pointer enable-button">
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
		<!-- Button for download -->
		<div>
			<button
				on:click={() => takeScreenshot()}
				class="px-3 py-2 ml-3 text-blue-500 transition duration-300 ease-in-out bg-transparent border-2 border-blue-500 rounded hover:bg-blue-500 hover:text-white"
			>
				Download new route
			</button>
		</div>
	</div>
</body>
