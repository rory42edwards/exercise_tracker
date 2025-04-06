import { Tracker } from './classes.js'

export function saveTrackerState(tracker) {
    localStorage.setItem('trackerState', JSON.stringify(tracker.workouts));
}

export function loadTrackerState() {
    const savedState = localStorage.getItem('trackerState');
    if (!savedState) return null;

    const tracker = new Tracker();
    tracker.loadWorkouts(JSON.parse(savedState));
    return tracker;
}
