from exercise_tracker.exercise_tracker import ExerciseTracker
from exercise_analysis.exercise_analyser import ExerciseAnalyser


def main() -> None:
    tracker = ExerciseTracker()
    analyser = ExerciseAnalyser()
    filename = 'data/workouts.json'
    tracker.load_from_file(filename)

    analyser.create_movements(tracker.workouts)
    # make plots for each movement
    for movement in analyser.movements:
        analyser.plot_load_over_time(movement)
        analyser.plot_load_volume_over_time(movement)

    # plot_exercises_per_workout(workouts)


if __name__ == '__main__':
    main()
