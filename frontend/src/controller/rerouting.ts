import pkg from 'mapbox-gl';
import type { Map } from 'mapbox-gl';
const { LngLatBounds } = pkg;
import { busNetwork, currentIndex, countReroute, rerouteIndex } from '../stores/stores';
import { get } from 'svelte/store';
import { drawDetailBusline } from './visualization';
const congestionColors: {
	[key: number]: string;
} = {
	0: '#43D224', // Congestion level 1
	1: '#FFE58F', // Congestion level 2
	2: '#FFA500', // Congestion level 3
	3: '#FC7A7A', // Congestion level 4
	4: '#B60606' // Congestion level 5
};

export async function fetchReroute(latlon1: [number, number], latlon2: [number, number], map:Map) {
	if (busNetwork == undefined) return;
	if (get(currentIndex) == -1 || get(currentIndex) == undefined) return;
    const accessToken: string = "pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg";
  
    function formatCoordinates(coordArray: number[]): string {
      return coordArray.map(coord => coord.toFixed(6)).join(',');
    }
	const bounds = new LngLatBounds(
		latlon1,
		latlon2
	);
  
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
		countReroute.update(current => current + 1);
		drawRerouting(data.routes[0], map, get(rerouteIndex));
		let busLines = get(busNetwork);
		let currentBusStop = busLines[get(currentIndex)][get(rerouteIndex)];
		let lineColor = map.getPaintProperty(`segment_${get(rerouteIndex)}`, 'line-color');
		let currentDistance = currentBusStop.properties.distance_m;
		let currentCongestionLevel = findCongestionLevelByColor(lineColor);
		let rerouteDistance = data.routes[0].distance;
		let rerouteCongestionLevel = findCongestionLevelByColor(mapSpeed(data.routes[0].legs[0].annotation.speed));
		map.fitBounds(bounds, {
			padding: { top: 200, bottom: 100, left: 300, right: 100 }
		});
		showPopup(currentDistance, currentCongestionLevel, rerouteDistance, rerouteCongestionLevel)
		.then((userChoice) => {
			// Handle user's choice here
			if (!userChoice) {
				removeReroute(map, get(rerouteIndex));
			} else {
				removeOriginalRoute(map, get(rerouteIndex));
			}
		})
		.catch((error) => {
			// Handle errors if any
			console.error('Error with popup:', error);
		})
		.finally(() => {
			drawDetailBusline(get(busNetwork), get(currentIndex), map);
		})
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
		const color = mapSpeed(route.legs[0].annotation.speed);
	  
		
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
				'line-width': 4,
			}
		});

		

}

function removeOriginalRoute(map: Map, index: number) {
	
	if (map.getLayer(`segment_${index}`)) {
	  map.removeLayer(`segment_${index}`);
	}
  }
  

  export function removeReroute(map: Map, index: number) {
	if (map.getLayer(`segment_reroute_${index}`)) {
	  map.removeLayer(`segment_reroute_${index}`);
	}
	if (map.getSource(`segment_reroute_${index}`)) {
	  map.removeSource(`segment_reroute_${index}`);
	}
  }
  

function mapSpeed(speeds: number[]) {
	const speed = speeds.reduce((total:number, num:number) => total + num, 0)  / speeds.length;
	const speedKmh = speed * 3.6; // Convert m/s to km/h
  
	if (speedKmh > 40) {
	  return congestionColors[0];
	} else if (speedKmh > 30 && speedKmh <= 40) {
	  return congestionColors[1];
	} else if (speedKmh > 20 && speedKmh <= 30) {
	  return congestionColors[2];
	} else if (speedKmh > 15 && speedKmh <= 20) {
	  return congestionColors[3];
	} else {
	  return congestionColors[4];
	}
  }



  export function deleteRerouteLayer(map: Map) {
	let max = get(countReroute);
	for (let i = 0; i <= max; i++) {
		if (map.getLayer(`segment_reroute_${i}`)) {
			map.removeLayer(`segment_reroute_${i}`);
		  }
		  if (map.getSource(`segment_reroute_${i}`)) {
			map.removeSource(`segment_reroute_${i}`);
		  }
	}
	
  }
  
  function findCongestionLevelByColor(colorCode: string) {
	switch (colorCode) {
		case '#43D224':
			return 0;
		case '#FFE58F':
			return 1;
		case '#FFA500':
			return 2;
		case '#FC7A7A':
			return 3;
		case '#B60606':
			return 4;
	}
}

function showPopup(
	currentDistance: number,
	currentCongestionLevel: number,
	rerouteDistance: number,
	rerouteCongestionLevel: number
  ): Promise<boolean> {
	return new Promise((resolve) => {
	  const modal = document.createElement('div');
	  modal.className = 'fixed inset-0 z-10 flex justify-end pt-4 pb-20 pr-4 mt-48 overflow-y-auto';
	  modal.innerHTML = `
	  <div class="inline-block overflow-hidden align-bottom transition-all transform bg-white rounded-lg shadow-xl w-fit h-fit">
	  <div class="px-4 pt-5 pb-4 bg-white">
		<div class="text-left">
		  <h3 class="mb-4 text-base font-medium leading-6 text-gray-900">Do you want to reroute?</h3>
		  <table class="border-collapse table-auto mb-4">
			<tbody>
				<tr>
				<td class="border px-3 py-2 text-sm text-gray-500">Property</td>
				<td class="border px-3 py-2 text-sm text-gray-500">Current</td>
				<td class="border px-3 py-2 text-sm text-gray-500">New</td>
				</tr>
				<tr>
				<td class="border px-3 py-2 text-sm text-gray-500">Distance (km)</td>
				<td class="border px-3 py-2 text-sm text-gray-500 text-center">${currentDistance.toFixed(2)}</td>
				<td class="border px-3 py-2 text-sm text-gray-500 text-center">${rerouteDistance.toFixed(2)}</td>
				</tr>
				<tr>
				<td class="border px-3 py-2 text-sm text-gray-500">Congestion</td>
				<td class="border px-3 py-2 text-sm text-gray-500 text-center">
					<span class="inline-block">
					<svg
						class="w-5 h-5 mr-1 inline-block align-middle"
						viewBox="0 0 20 20"
						fill="${congestionColors[currentCongestionLevel]}"
						xmlns="http://www.w3.org/2000/svg"
					>
					<path xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" d="M12 2C8.22876 2 6.34315 2 5.17157 3.17157C4.10848 4.23467 4.01004 5.8857 4.00093 9H3C2.44772 9 2 9.44772 2 10V11C2 11.3148 2.14819 11.6111 2.4 11.8L4 13C4.00911 16.1143 4.10848 17.7653 5.17157 18.8284C5.41375 19.0706 5.68645 19.2627 6 19.4151V20.9999C6 21.5522 6.44772 21.9999 7 21.9999H8.5C9.05228 21.9999 9.5 21.5522 9.5 20.9999V19.9815C10.2271 20 11.0542 20 12 20C12.9458 20 13.7729 20 14.5 19.9815V20.9999C14.5 21.5522 14.9477 21.9999 15.5 21.9999H17C17.5523 21.9999 18 21.5522 18 20.9999V19.4151C18.3136 19.2627 18.5862 19.0706 18.8284 18.8284C19.8915 17.7653 19.9909 16.1143 20 13L21.6 11.8C21.8518 11.6111 22 11.3148 22 11V10C22 9.44772 21.5523 9 21 9H19.9991C19.99 5.8857 19.8915 4.23467 18.8284 3.17157C17.6569 2 15.7712 2 12 2ZM5.5 9.5C5.5 10.9142 5.5 11.6213 5.93934 12.0607C6.37868 12.5 7.08579 12.5 8.5 12.5H12H15.5C16.9142 12.5 17.6213 12.5 18.0607 12.0607C18.5 11.6213 18.5 10.9142 18.5 9.5V7C18.5 5.58579 18.5 4.87868 18.0607 4.43934C17.6213 4 16.9142 4 15.5 4H12H8.5C7.08579 4 6.37868 4 5.93934 4.43934C5.5 4.87868 5.5 5.58579 5.5 7V9.5ZM6.25 16C6.25 15.5858 6.58579 15.25 7 15.25H8.5C8.91421 15.25 9.25 15.5858 9.25 16C9.25 16.4142 8.91421 16.75 8.5 16.75H7C6.58579 16.75 6.25 16.4142 6.25 16ZM17.75 16C17.75 15.5858 17.4142 15.25 17 15.25H15.5C15.0858 15.25 14.75 15.5858 14.75 16C14.75 16.4142 15.0858 16.75 15.5 16.75H17C17.4142 16.75 17.75 16.4142 17.75 16Z"/>
					</svg>
					</span>
				</td>
				<td class="border px-3 py-2 text-sm text-gray-500 text-center">
					<span class="inline-block">
					<svg
						class="w-5 h-5 mr-1 inline-block align-middle"
						viewBox="0 0 20 20"
						fill="${congestionColors[rerouteCongestionLevel]}"
						xmlns="http://www.w3.org/2000/svg"
					>
					<path xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" d="M12 2C8.22876 2 6.34315 2 5.17157 3.17157C4.10848 4.23467 4.01004 5.8857 4.00093 9H3C2.44772 9 2 9.44772 2 10V11C2 11.3148 2.14819 11.6111 2.4 11.8L4 13C4.00911 16.1143 4.10848 17.7653 5.17157 18.8284C5.41375 19.0706 5.68645 19.2627 6 19.4151V20.9999C6 21.5522 6.44772 21.9999 7 21.9999H8.5C9.05228 21.9999 9.5 21.5522 9.5 20.9999V19.9815C10.2271 20 11.0542 20 12 20C12.9458 20 13.7729 20 14.5 19.9815V20.9999C14.5 21.5522 14.9477 21.9999 15.5 21.9999H17C17.5523 21.9999 18 21.5522 18 20.9999V19.4151C18.3136 19.2627 18.5862 19.0706 18.8284 18.8284C19.8915 17.7653 19.9909 16.1143 20 13L21.6 11.8C21.8518 11.6111 22 11.3148 22 11V10C22 9.44772 21.5523 9 21 9H19.9991C19.99 5.8857 19.8915 4.23467 18.8284 3.17157C17.6569 2 15.7712 2 12 2ZM5.5 9.5C5.5 10.9142 5.5 11.6213 5.93934 12.0607C6.37868 12.5 7.08579 12.5 8.5 12.5H12H15.5C16.9142 12.5 17.6213 12.5 18.0607 12.0607C18.5 11.6213 18.5 10.9142 18.5 9.5V7C18.5 5.58579 18.5 4.87868 18.0607 4.43934C17.6213 4 16.9142 4 15.5 4H12H8.5C7.08579 4 6.37868 4 5.93934 4.43934C5.5 4.87868 5.5 5.58579 5.5 7V9.5ZM6.25 16C6.25 15.5858 6.58579 15.25 7 15.25H8.5C8.91421 15.25 9.25 15.5858 9.25 16C9.25 16.4142 8.91421 16.75 8.5 16.75H7C6.58579 16.75 6.25 16.4142 6.25 16ZM17.75 16C17.75 15.5858 17.4142 15.25 17 15.25H15.5C15.0858 15.25 14.75 15.5858 14.75 16C14.75 16.4142 15.0858 16.75 15.5 16.75H17C17.4142 16.75 17.75 16.4142 17.75 16Z"/>
					</svg>
					</span>
				</td>
				</tr>
			</tbody>
			</table>


		  <button class="inline-flex justify-center w-full px-4 py-2 mt-2 text-base font-medium text-white bg-blue-500 border border-transparent rounded-md shadow-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 sm:text-sm">Yes</button>
		  <button class="inline-flex justify-center w-full px-4 py-2 mt-2 text-base font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 sm:text-sm">No</button>
		</div>
	  </div>
	</div>
	
	  `;
  
	  // Function to handle button click
	  function handleClick(choice: boolean) {
		resolve(choice);
		modal.remove();
	  }
  
	  // Get buttons and attach event listeners
	  modal.querySelectorAll('button').forEach((button, index) => {
		button.addEventListener('click', () => {
		  const isYesButton = index === 0; // Assuming Yes button is the first button
		  handleClick(isYesButton);
		});
	  });
  
	  document.body.appendChild(modal);
	});
  }
  