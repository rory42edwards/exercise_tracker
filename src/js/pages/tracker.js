import { renderWorkouts } from '../modules/trackerUI.js'
import { Tracker } from '../modules/classes.js'
import { saveTrackerState, loadTrackerState } from '../modules/trackerState.js'
import { saveTracker, fetchData } from '../modules/trackerAPI.js'

function handleAction(type, payload, tracker) {
    switch (type) {
        case 'removeWorkout':
            tracker.removeWorkout(payload);
            break;
        case 'saveTracker':
            saveTracker(payload);
            break;
    }

    saveTrackerState(tracker);
    renderWorkouts(tracker);
}

async function init() {
    const data = await fetchData();
    const tracker = new Tracker();
    tracker.loadWorkouts(data);
    renderWorkouts(tracker);
    saveTrackerState(tracker);
    

    document.getElementById('workoutHistoryContainer').addEventListener('click', (event) => {
        const button = event.target.closest('button');
        if (!button) return;

        const action = button.dataset.action;
        if (!action) return;

        switch (action) {
            case 'removeWorkout':
                console.log("trying to remove workout");
                handleAction('removeWorkout', button.dataset.date, tracker);
                break;

            case 'saveTracker':
                console.log("trying to save");
                handleAction('saveTracker', tracker.workouts, tracker);
                break;

            default:
                console.warn('Unhandled action: ', action);
        }
    });
}

window.addEventListener('DOMContentLoaded', init);
