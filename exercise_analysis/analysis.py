import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from movement import Movement
from datetime import datetime


def get_exercises(exercises):
    # create unique list of exercise names
    exercise_names = []
    for exercise in exercises:
        # print(exercise['name'])
        if exercise['name'] not in exercise_names:
            exercise_names.append(exercise['name'])
    return exercise_names


def create_movements(exercise_names, exercises):
    movements = [Movement(name) for name in exercise_names]

    for movement in movements:
        # print(exercise['name'])
        # print(exercise['date'])
        # print(exercise['sets'])
        for exercise in exercises:
            if exercise['name'] == movement.name:
                movement.add_workout(exercise['date'], exercise['sets'])
        # print(movement)
    return movements


def plot_exercises_per_workout(exercises):
    dates = [datetime.fromisoformat(exercise['date'])
             for exercise in exercises]

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


def main():
    filename = '../data/exercises.json'
    with open(filename, 'r') as f:
        exercises = json.load(f)

    exercise_names = get_exercises(exercises)
    movements = create_movements(exercise_names, exercises)

    # make plots for each movement

    plot_exercises_per_workout(exercises)


if __name__ == '__main__':
    main()
