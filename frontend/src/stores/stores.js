import { writable } from 'svelte/store';

export const searchPopoverVisible = writable(true);
export const busLinePopoverVisible = writable(false);
export const busStopPopoverVisible = writable(false);
export const currentBusLine = writable(0);
export const currentBusStop = writable(0);
