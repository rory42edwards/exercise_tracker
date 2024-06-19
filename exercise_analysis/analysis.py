import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from exercise_tracker.exercise import Exercise
from exercise_analysis.movement import Movement
from datetime import datetime


def get_exercises(workouts: list[dict]) -> list[str]:
    # create unique list of exercise names
    exercise_names = []
    for workout in workouts:
        print(workout)
        for exercise in workout['exercises']:
            print(exercise)
            if exercise['name'] not in exercise_names:
                exercise_names.append(exercise['name'])
    return exercise_names


def create_movements(exercise_names: list[str],
                     workouts: dict) -> list[Movement]:
    movements = [Movement(name) for name in exercise_names]

    for movement in movements:
        # print(exercise['name'])
        # print(exercise['date'])
        # print(exercise['sets'])
        for workout in workouts:
            for exercise in workout['exercises']:
                if exercise['name'] == movement.name:
                    movement.add_workout(workout['date'], exercise['sets'])
        # print(movement)
    return movements


def plot_exercises_per_workout(exercises: dict) -> None:
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


def plot_load_over_time(movement: Movement) -> None:
    dates = []
    highest_loads = []
    print(f"Exercise: {movement.name}")
    for date, sets in movement.all_sets.items():
        date = datetime.fromisoformat(date)
        dates.append(date)
        loads = []
        for pair in sets:
            try:
                # if load is number in kg, add that to loads
                loads.append(float(pair[1]))
            except ValueError:
                try:
                    # if load is something like 'bw',
                    # add 0 to loads to show weight added over time
                    loads.append(0)
                except ValueError:
                    continue
        try:
            highest_loads.append(max(loads))
        except ValueError:
            continue
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


def main() -> None:
    filename = 'data/workouts.json'
    with open(filename, 'r') as f:
        workouts = json.load(f)

    exercise_names = get_exercises(workouts)
    movements = create_movements(exercise_names, workouts)

    # make plots for each movement
    for movement in movements:
        plot_load_over_time(movement)

    plot_exercises_per_workout(workouts)


if __name__ == '__main__':
    main()
