from exercise import Exercise
import json


class ExerciseTracker:
    def __init__(self, date):
        self.exercises = []
        self.exercise_names = []
        self.date = date

    def add_exercise(self, name):
        exercise = Exercise(name, self.date)
        self.exercises.append(exercise)
        if name not in self.exercise_names:
            self.exercise_names.append(name)

    def get_exercise(self, name):
        for exercise in self.exercises:
            if exercise.name == name:
                return exercise
        return None

    def show_exercises(self):
        for name in self.exercise_names:
            print(name)

    def show_all_exercises(self):
        for exercise in self.exercises:
            print(exercise)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([exercise.to_dict()
                       for exercise in self.exercises], f, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            exercises_data = json.load(f)
            self.exercises =\
                [Exercise.from_dict(data) for data in exercises_data]
