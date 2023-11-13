import { writable } from 'svelte/store';

export const allBusLines = writable([] as AllBusLines);
export const currentIndex = writable(-1);
export const minute = writable(0);
