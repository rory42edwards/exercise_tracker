from exercise import Exercise
import json


class ExerciseTracker:
    def __init__(self):
        self.exercises = []
        self.exercise_names = []

    def add_exercise(self, name, date):
        exercise = Exercise(name, date)
        self.exercises.append(exercise)
        length = len(self.exercise_names)
        if name not in self.exercise_names:
            self.exercise_names.append([length+1, name])

    def get_exercise_name(self, index):
        for names in self.exercise_names:
            if names[0] == int(index):
                return names[1]
        return None  # if no match found

    def get_exercise(self, name, date):
        for exercise in self.exercises:
            if exercise.name == name and exercise.date == date:
                return exercise
        return None  # if no match found

    def show_exercises(self):
        for name in self.exercise_names:
            print(f"{name[0]}: {name[1]}")

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
