// @ts-ignore
export function getCenterLngLat(formatedBuslines) {
	let lng = 0;
	let lat = 0;
	let length = 0;
	if (formatedBuslines == undefined) return;
	// if (initialState.center) return initialState.center;
	// @ts-ignore
	formatedBuslines.forEach((formatedBusline) => {
		// @ts-ignore
		formatedBusline.forEach((busStop) => {
			// @ts-ignore
			busStop.geometry.coordinates.forEach((coordinate) => {
				lng += coordinate[0];
				lat += coordinate[1];
				length++;
			});
		});
	});
	return [lng / length, lat / length];
}
