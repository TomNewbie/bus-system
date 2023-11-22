import { writable } from 'svelte/store';

export const busNetwork = writable([] as BusNetwork);
export const currentIndex = writable(-1);
export const minute = writable(0);
export const model = writable('lstm');
export const isToastShowed = writable(false);