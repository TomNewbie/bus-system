import { writable } from 'svelte/store';

export const busNetwork = writable([] as BusNetwork);
export const currentIndex = writable(-1);
export const minute = writable(0);
