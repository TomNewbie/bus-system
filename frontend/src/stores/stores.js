import { writable } from 'svelte/store';

export const allBusLines = writable(undefined);
export const currentIndex = writable(-1);
export const minute = writable(0);
