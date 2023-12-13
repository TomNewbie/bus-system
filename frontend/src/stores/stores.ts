import { writable } from 'svelte/store';

export const busNetwork = writable([] as BusNetwork);
export const currentIndex = writable(-1);
export const minute = writable(0);
export const model = writable('lstm');
export const isToastShowed = writable(false);
export const canReroute = writable(false);
export const reroutingMode = writable(false);
export const start_stop_lon_lat = writable([]);
export const end_stop_lon_lat = writable([]);
export const countReroute = writable(0)
