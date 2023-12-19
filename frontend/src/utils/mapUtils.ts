export function getCenterLngLat(initialState: MapState, formatedBuslines: BusNetwork) {
	let lng = 0;
	let lat = 0;
	let length = 0;
	if (formatedBuslines == undefined) return;
	if (initialState.center) return initialState.center;
	formatedBuslines.forEach((formatedBusline) => {
		formatedBusline.forEach((busStop) => {
			busStop.geometry.coordinates.forEach((coordinate) => {
				lng += coordinate[0];
				lat += coordinate[1];
				length++;
			});
		});
	});
	initialState.center = [lng / length, lat / length];
	return initialState.center;
}
