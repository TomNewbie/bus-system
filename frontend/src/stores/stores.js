import { writable } from 'svelte/store';

export const searchPopoverVisible = writable(true);
export const busLinePopoverVisible = writable(false);
export const busStopPopoverVisible = writable(false);
