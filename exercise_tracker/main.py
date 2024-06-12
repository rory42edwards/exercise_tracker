from datetime import datetime
from exercise_tracker import ExerciseTracker


def main():
    date_string = input("Enter date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%y")
    tracker = ExerciseTracker()

    filename = '../data/exercises.json'
    try:
        tracker.load_from_file(filename)
        print("exercises.json loaded successfully.")
    except FileNotFoundError:
        print("exercises.json not found. Starting a new one.")

    # check for duplicate date in datebase
    for exercise in tracker.exercises:
        if date == exercise.date:
            response = input("Date already found\
 in database! Are you sure you want to continue? [y/n] ")
            if response.lower() == 'n':
                exit()

    while True:
        # print options to user
        print("1. Add new exercise")
        print("2. Add set to exercise")
        print("3. Show all exercises")
        print("4. Save and exit")
        choice = input("Enter option: ")

        if choice == '1':
            name = input("Enter exercise name: ")
            tracker.add_exercise(name, date)
        elif choice == '2':
            tracker.show_exercises()
            index = input("Enter exercise: ")
            name = tracker.get_exercise_name(index)
            exercise = tracker.get_exercise(name, date)
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
            tracker.show_all_exercises()
        elif choice == '4':
            tracker.save_to_file(filename)
            print("Exercises saved. Exiting.")
            break
        else:
            print("Not a valid option. Try again.")


if __name__ == "__main__":
    main()
