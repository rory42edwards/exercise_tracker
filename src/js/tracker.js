import { renderWorkouts, loadState, saveState } from './trackerDOM.js';

class Set {
    constructor (reps, load) {
        this.reps = parseInt(reps);
        this.load = parseFloat(load);
    }
}

class Exercise {
    constructor (name) {
        this.name = name.toLowerCase();
        this.sets = []
    }

    addSet (reps, load) {
        const set = new Set(reps, load);
        this.sets.push(set)
    }
}

class Workout {
    constructor (date) {
        this.date = date
        this.exercises = []
    }

    addExercise (name) {
        const exercise = new Exercise(name)
        this.exercises.push(exercise)
    }

    getExercise (name) {
        return this.exercises.find(exercise => exercise.name === name);
    }

    removeExercise (name) {
        const index = this.exercises.findIndex(exercise => exercise.name === name);

        if (index !==-1) {
            this.exercises.splice(index, 1);
        }
    }
}

export class Tracker {
    constructor () {
        this.workouts = []
    }

    addWorkout (date) {
        const workout = new Workout(date)
        this.workouts.push(workout)
    }

    getWorkout (date) {
        return this.workouts.find(workout => workout.date === date);
    }

    removeWorkout (date) {
        const index = this.workouts.findIndex(workout => workout.date === date);

        if (index !==-1) {
            this.workouts.splice(index, 1);
        }
    }

    loadWorkouts (data) {
        //this.workouts = data;
        if (!Array.isArray(data)) {
            throw new Error('Data must be an array');
        }
        this.workouts = data.map(workoutData => {
            const workout = new Workout(workoutData.date);
            workout.exercises = workoutData.exercises.map(exerciseData => {
                const exercise = new Exercise(exerciseData.name);
                exercise.sets = exerciseData.sets.map(setData => new Set(setData.reps, setData.load));
                return exercise;
            });
            return workout;
        });
    }

    workoutsByDate () {
        let dates = [];
        this.workouts.forEach( workout => {
            dates.push(workout.date);
        });
        const sortedDates = dates.toSorted();
        let sortedWorkouts = [];
        sortedDates.forEach(date => {
            this.workouts.forEach(workout => {
                if (date == workout.date) {
                    sortedWorkouts.push(workout);
                }
            });
        });
        sortedWorkouts.reverse();
        return sortedWorkouts;
    }
}

async function fetchData() {
    try {
        const response = await fetch('/api/get_data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
            console.error('Problem with fetch operation: ', error);
        }
}

async function init() {
    const data = await fetchData();
    if (data) {
        const tracker = new Tracker();
        tracker.loadWorkouts(data);
        renderWorkouts(tracker);
        saveState(tracker);
    }
}

window.onload = () => {
    const tracker = loadState();
    if (tracker) {
        renderWorkouts(tracker);
    } else {
        init();
    }
};
