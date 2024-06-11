import matplotlib.pyplot as plt
import json
from movement import Movement


def main():
    filename = '../data/exercises.json'
    with open(filename, 'r') as f:
        exercises = json.load(f)

    # create unique list of exercise names
    exercise_names = []
    for exercise in exercises:
        # print(exercise['name'])
        if exercise['name'] not in exercise_names:
            exercise_names.append(exercise['name'])

    # create a list of movement
    movements = [Movement(name) for name in exercise_names]

    for movement in movements:
        # print(exercise['name'])
        # print(exercise['date'])
        # print(exercise['sets'])
        for exercise in exercises:
            if exercise['name'] == movement.name:
                movement.add_workout(exercise['date'], exercise['sets'])
        print(movement)


if __name__ == '__main__':
    main()
