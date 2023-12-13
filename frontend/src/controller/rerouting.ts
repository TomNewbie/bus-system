import type { Map } from 'mapbox-gl';
import { countReroute } from '../stores/stores';
import { get } from 'svelte/store';
const congestionColors: {
	[key: number]: string;
} = {
	0: '#43D224', // Congestion level 1
	1: '#FFE58F', // Congestion level 2
	2: '#FE6240', // Congestion level 3
	3: '#fc7a7a', // Congestion level 4
	4: '#B60606' // Congestion level 5
};

export async function fetchReroute(latlon1: number[], latlon2: number[], map:Map): Promise<any> {
	if(latlon1.length == 0 && latlon2.length == 0) return;
    const accessToken: string = "pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg";
  
    function formatCoordinates(coordArray: number[]): string {
      return coordArray.map(coord => coord.toFixed(6)).join(',');
    }
  
    const formattedLatLon1: string = formatCoordinates(latlon1);
    const formattedLatLon2: string = formatCoordinates(latlon2);
  
    const apiUrl: string = `https://api.mapbox.com/directions/v5/mapbox/driving/${formattedLatLon1};${formattedLatLon2}?alternatives=true&annotations=speed%2Cdistance&geometries=geojson&language=en&overview=full&steps=true&access_token=${accessToken}`;
  
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
		countReroute.update(current => current + 1);
		drawRerouting(data.routes[0], map, get(countReroute));
		setTimeout(() => {
            if (!confirm('Do you want to choose a new route?')) {
                removeReroute(map, get(countReroute));
            }
        }, 500);
		})
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        throw error;
      });
  }

  function drawRerouting(
	route: any,
	map: Map,
	index: any
) {
		
		// Determine the color based on congestion level
		const speeds = route.legs[0].annotation.speed;
		const speed = speeds.reduce((total:number, num:number) => total + num, 0)  / speeds.length;
		const colorIndex = mapSpeed(speed);
	  
		const color = congestionColors[colorIndex];
		
		// Create a source and layer for each segment
		map.addSource(`segment_reroute_${index}`, {
			type: 'geojson',
			data: {
				type: 'Feature',
				//@ts-ignore
				properties: {},
				geometry: route.geometry
			}
		});

		map.addLayer({
			id: `segment_reroute_${index}`,
			type: 'line',
			source: `segment_reroute_${index}`,
			layout: {
				'line-join': 'miter',
				'line-cap': 'square'
			},
			paint: {
				'line-color': color,
				'line-width': 10,
				'line-opacity': 0.5
			}
		});

		

}

export function removeReroute(map: Map, index: number) {
	if (map.getLayer(`segment_reroute_${index}`)) {
	  map.removeLayer(`segment_reroute_${index}`);
	}
	if (map.getSource(`segment_reroute_${index}`)) {
	  map.removeSource(`segment_reroute_${index}`);
	}
  }
  

function mapSpeed(speedMs: number) {
	const speedKmh = speedMs * 3.6; // Convert m/s to km/h
  
	if (speedKmh > 40) {
	  return 0;
	} else if (speedKmh > 30 && speedKmh <= 40) {
	  return 1;
	} else if (speedKmh > 20 && speedKmh <= 30) {
	  return 2;
	} else if (speedKmh > 15 && speedKmh <= 20) {
	  return 3;
	} else {
	  return 4;
	}
  }
