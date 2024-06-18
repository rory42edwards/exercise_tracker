from exercise_tracker.exercise import Exercise
from datetime import datetime


class Workout:
    """
    A class which holds multiple exercise objects for a single date
    """

    def __init__(self, date):
        self.date = date
        self.exercises = []
        self.exercise_names = []

    def add_exercise(self, name):
        exercise = Exercise(name)
        self.exercises.append(exercise)
        length = len(self.exercise_names)
        if name not in self.exercise_names:
            self.exercise_names.append([length+1, name])

    def show_exercises(self):
        for name in self.exercise_names:
            print(f"{name[0]}: {name[1]}")

    def show_all_exercises(self):
        print(f"Workout on: {self.date}")
        for exercise in self.exercises:
            print(exercise)

    def get_exercise(self, name):
        for exercise in self.exercises:
            if exercise.name == name:
                return exercise
        return None  # if no match found

    def get_exercise_name(self, index):
        name = next((names[1] for
                    names in self.exercise_names if
                     names[0] == int(index)), None)
        return name

    def to_dict(self):
        return {'date': self.date.isoformat(),
                'exercises': [exercise.to_dict()
                              for exercise in self.exercises]
                }

    @classmethod
    def from_dict(cls, data):
        workout = cls(datetime.fromisoformat(data['date']))
        workout.exercises = [Exercise.from_dict(ex) for
                             ex in data['exercises']]
        return workout

    def __str__(self):
        return f"Workout on: {self.date}"
