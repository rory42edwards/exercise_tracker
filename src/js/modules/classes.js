export class Set {
    constructor (reps, load, rpe=-1) {
        this.reps = parseInt(reps);
        this.load = parseFloat(load);
        this.rpe = parseInt(rpe);
    }
}

export class Exercise {
    constructor (name) {
        this.name = name.toLowerCase();
        this.sets = []
    }

    addSet (reps, load, rpe) {
        const set = new Set(reps, load, rpe);
        this.sets.push(set)
    }
}

export class Workout {
    constructor (date, title) {
        this.title = title
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

    loadExercises (data) {
        if (!Array.isArray(data)) {
            throw new Error('Data must be an array');
        }
        this.exercises = data.map(exerciseData => {
            const exercise = new Exercise(exerciseData.name);
            exercise.sets = exerciseData.sets.map(setData => new Set(setData.reps, setData.load));
            return exercise;
        });
    }

    hasDate (date) {
        if (this.date === date) return true;
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

    hasDate (date) {
        this.workouts.forEach( workout => {
            if (workout.hasDate(date)) return true;
        });
        return false;
    }
}
