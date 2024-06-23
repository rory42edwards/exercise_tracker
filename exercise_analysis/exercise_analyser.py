from exercise_analysis.movement import Movement
from exercise_tracker.workout import Workout
from datetime import datetime
from typing import Type, Union
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class ExerciseAnalyser:
    def __init__(self):
        self.movements = []

    def create_movements(self, workouts: list['Workout']) -> None:
        # create unique list of exercise names
        exercise_names = []
        for workout in workouts:
            # print(workout)
            for exercise in workout.exercises:
                # print(exercise)
                if exercise.name not in exercise_names:
                    exercise_names.append(exercise.name)
        movements = [Movement(name) for name in exercise_names]

        for movement in movements:
            for workout in workouts:
                for exercise in workout.exercises:
                    if exercise.name == movement.name:
                        movement.add_workout(workout.date, exercise.sets)
            self.movements.append(movement)

    def plot_exercises_per_workout(self, workouts: list[Type['Workout']]) -> None:
        dates = [workout.date for workout in workouts]
        number_of_exercises = [len(workout.exercises) for workout in workouts]

        fig, ax = plt.subplots()
        ax.hist(dates, bins=30, rwidth=0.8)
        ax.xaxis.set_major_locator(mdates.WeekdayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

        plt.xlabel('Date')
        plt.ylabel('Frequency')
        plt.title('Exercise Frequency Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_load_over_time(self, movement: Movement) -> None:
        dates = []
        highest_loads = []
        print(f"Exercise: {movement.name}")
        for date, sets in movement.all_sets.items():
            # date = datetime.fromisoformat(date)
            dates.append(date)
            loads = []
            for pair in sets:
                loads.append(float(pair[1]))
            highest_loads.append(max(loads))
            print(f"{date}: {loads}")
        print(f"{highest_loads}")
        if len(dates) != len(highest_loads):
            print("Dates and highest_loads not same size! Skipping...")
            return None
        plt.scatter(dates, highest_loads, label=f"{movement.name} - Load")
        plt.xlabel("Date")
        plt.ylabel("Load / kg")
        plt.title(f"Load over time: {movement.name}")
        plt.xticks(rotation=45)
        plt.show()

    def get_movement(self, name: str) -> Union[Movement, None]:
        for movement in self.movements:
            if movement.name.lower() == name.lower():
                return movement
        return None
