export async function fetchBusLine(api: any) {
	let a = [];
	try {
		const response = await fetch(`${api}/segments`);
		if (response.ok) {
			const data: GeoJsonWithId[] = await response.json();
			// Process the data and remove the "_id" attribute
			a = data.map((item: any) => {
				const { _id, ...itemWithoutId } = item;
				return itemWithoutId;
			});
		} else {
			alert('Request failed with status: ' + response.status);
		}
	} catch (error) {
		alert('Error while fetching data: ' + error);
	}
	const groupedData: GeoJsonGroupByShapeId = {};
	a.forEach((feature) => {
		const shapeId = feature.properties.shape_id;
		if (!groupedData[shapeId]) {
			groupedData[shapeId] = [];
		}
		groupedData[shapeId].push(feature);
	});
	return Object.values(groupedData);
}

export async function fetchCongestionDataByBusline(
	apiUrl: string,
	model: string,
	route_id: string,
	shape_id: string,
	direction_id: number,
	minute: number,
	abortController: AbortController
) {
	if (minute == 0) return;
	// fetch data
	let result;
	let abortSignal = abortController.signal;
	try {
		const response = await fetch(
			`${apiUrl}/predict/${model}?route_id=${route_id}&shape_id=${shape_id}&direction_id=${direction_id}&minute_predict=${minute}`,
			{ signal: abortSignal }
		);
		if (response.ok) {
			const data = await response.json();
			// Process the data and remove the "_id" attribute
			//@ts-ignore
			result = data.map((item) => {
				const { _id, ...itemWithoutId } = item;
				return itemWithoutId;
			});
		} else {
			alert('Request failed with status: ' + response.status);
			return;
		}
	} catch (error) {
		alert('Error while fetching data: ' + error);
		return;
	}
	return result;
}
