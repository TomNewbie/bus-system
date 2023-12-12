import type { Map } from 'mapbox-gl';
import { setDisableLayer } from './visualization';

export async function fetchReroute(latlon1: number[], latlon2: number[], map:Map): Promise<any> {
	if(latlon1.length == 0 && latlon2.length == 0) return;
    const accessToken: string = "pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg";
  
    function formatCoordinates(coordArray: number[]): string {
      return coordArray.map(coord => coord.toFixed(6)).join(',');
    }
  
    const formattedLatLon1: string = formatCoordinates(latlon1);
    const formattedLatLon2: string = formatCoordinates(latlon2);
  
    const apiUrl: string = `https://api.mapbox.com/directions/v5/mapbox/driving/${formattedLatLon1};${formattedLatLon2}?alternatives=false&annotations=speed%2Cdistance&geometries=geojson&language=en&overview=full&steps=true&access_token=${accessToken}`;
  
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
		console.log(data);
        let result  = data.routes[0].geometry.coordinates;
        drawRerouting(data.routes[0], map);
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        throw error;
      });
  }

  function drawRerouting(
	route: any,
	map: Map
) {


	// currentBusLine.forEach((segment, segmentIndex) => {
		// Access the congestion level of the segment
		// const congestionLevel = segment.congestion_level;
		
		// Determine the color based on congestion level
		const color = 'black';
		console.log(route.geometry);
		// Create a source and layer for each segment
		map.addSource(`segment_redirect`, {
			type: 'geojson',
			data: {
				type: 'Feature',
				//@ts-ignore
				properties: {},
				geometry: route.geometry
			}
		});

		map.addLayer({
			id: `segment_redirect`,
			type: 'line',
			source: `segment_redirect`,
			layout: {
				'line-join': 'miter',
				'line-cap': 'round'
			},
			paint: {
				'line-color': color,
				'line-width': 20
			}
		});
}