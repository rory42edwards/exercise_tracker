from datetime import datetime
from exercise_tracker.exercise_tracker import ExerciseTracker


def add_new_workout(tracker: ExerciseTracker) -> None:
    date_string = input("Enter date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%y")

    # check for duplicate date in datebase
    for workout in tracker.workouts:
        if date == workout.date:
            response = input("Date already found\
 in database! Are you sure you want to continue? [y/n] ")
            if response.lower() == 'n':
                exit()
    tracker.add_workout(date)
    workout = tracker.get_workout(date)

    while True:
        print("1. Add exercise")
        print("2. Add set to exercise")
        print("3. Show workout")
        print("4. Save and return to tracker")
        choice = input("Enter option: ")

        if choice == '1':
            name = input("Enter exercise name: ")
            workout.add_exercise(name)

        elif choice == '2':
            workout.show_exercises()
            index = input("Enter exercise: ")
            name = workout.get_exercise_name(index)
            exercise = workout.get_exercise(name)
            if exercise:
                print(f"Adding set to {name}:")
                reps = int(input("Enter number of reps: "))
                load = input("Enter load: ")
                exercise.add_set(reps, load)
                set_counter = 1
                while True:
                    more_sets = input("Add multiple sets? [y/n] ")
                    if more_sets.lower() == 'n':
                        break
                    exercise.add_set(reps, load)
                    set_counter += 1
                    print("Adding another set...")
                if set_counter == 1:
                    print(f"Added {set_counter} set to {name}.")
                else:
                    print(f"Added {set_counter} sets to {name}.")
            else:
                print("Exercise not found. Add it to the list.")

        elif choice == '3':
            workout.show_all_exercises()

        elif choice == '4':
            break


def print_tracker_console(tracker: ExerciseTracker, filename: str):
    while True:
        print("1. Add new workout")
        print("2. Show all workouts")
        print("3. Save and exit")
        choice = input("Enter option: ")

        if choice == '1':
            add_new_workout(tracker)

        elif choice == '2':
            tracker.show_all_workouts()

        elif choice == '3':
            tracker.save_to_file(filename)
            print("Exercises saved. Exiting.")
            break

        else:
            print("Not a valid option. Try again.")


def main() -> None:
    tracker = ExerciseTracker()

    filename = 'data/workouts.json'
    try:
        tracker.load_from_file(filename)
        print(f"{filename} loaded successfully.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting a new one.")

    print_tracker_console(tracker, filename)


if __name__ == "__main__":
    main()
