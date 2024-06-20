from exercise_tracker.exercise import Exercise
from datetime import datetime
from typing import Type, Union


class Workout:
    """
    A class which holds multiple exercise objects for a single date
    """

    def __init__(self, date: datetime):
        if isinstance(date, str):
            self.date = datetime.strptime(date, "%Y-%m-%d")
        elif isinstance(date, datetime):
            self.date = date
        else:
            raise ValueError("Invalid date type. Must be string or datetime.")
        self.exercises: list[Exercise] = []
        self.exercise_names: list[list] = []

    def add_exercise(self, name: str) -> None:
        exercise = Exercise(name)
        self.exercises.append(exercise)
        length = len(self.exercise_names)
        if name not in self.exercise_names:
            self.exercise_names.append([length+1, name])

    def show_exercises(self) -> None:
        for name in self.exercise_names:
            print(f"{name[0]}: {name[1]}")

    def show_all_exercises(self) -> None:
        print(f"Workout on: {self.date}")
        for exercise in self.exercises:
            print(exercise)

    def get_exercise(self, name: str) -> Union[Exercise, None]:
        for exercise in self.exercises:
            if exercise.name == name:
                return exercise
        return None  # if no match found

    def get_exercise_name(self, index: str) -> Union[str, None]:
        name = next((names[1] for
                    names in self.exercise_names if
                     names[0] == int(index)), None)
        return name

    def to_dict(self) -> dict:
        return {'date': self.date.isoformat(),
                'exercises': [exercise.to_dict()
                              for exercise in self.exercises]
                }

    @classmethod
    def from_dict(cls: Type['Workout'], data: dict) -> 'Workout':
        workout = cls(datetime.fromisoformat(data['date']))
        workout.exercises = [Exercise.from_dict(ex) for
                             ex in data['exercises']]
        return workout

    def __str__(self):
        return f"Workout on: {self.date}"
