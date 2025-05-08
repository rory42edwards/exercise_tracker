import { Workout } from './classes.js'

export function saveWorkoutState(workout) {
    localStorage.setItem('workoutState', JSON.stringify(workout));
}

export function loadWorkoutState() {
    const savedState = localStorage.getItem('workoutState');
    if (!savedState) return null;

    const data = JSON.parse(savedState);
    return Workout.fromObject(data);
}
