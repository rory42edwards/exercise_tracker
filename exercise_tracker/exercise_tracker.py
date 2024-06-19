from exercise_tracker.workout import Workout
from datetime import datetime
from typing import Union
import json


class ExerciseTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, date: datetime) -> None:
        workout = Workout(date)
        self.workouts.append(workout)

    def get_workout(self, date: datetime) -> Union[Workout, None]:
        for workout in self.workouts:
            if workout.date == date:
                return workout
        return None  # if no match found

    def show_all_workouts(self) -> None:
        for workout in self.workouts:
            print(workout)

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump([workout.to_dict()
                       for workout in self.workouts], f, indent=4)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            workouts_data = json.load(f)
            self.workouts =\
                [Workout.from_dict(data) for data in workouts_data]
