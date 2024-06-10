from datetime import datetime
from exercise_tracker import ExerciseTracker


def main():
    date_string = input("Enter date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%y")
    tracker = ExerciseTracker(date)

    try:
        tracker.load_from_file('exercises.json')
        print("exercise.json loaded successfully.")
    except FileNotFoundError:
        print("exercise.json not found. Starting a new one.")

    while True:
        print("1. Add new exercise")
        print("2. Add set to exercise")
        print("3. Show all exercises")
        print("4. Save and exit")
        choice = input("Enter option: ")

        if choice == '1':
            name = input("Enter exercise name: ")
            tracker.add_exercise(name)
        elif choice == '2':
            name = input("Enter exercise name: ")
            tracker.show_exercises()
            exercise = tracker.get_exercise(name)
            if exercise:
                reps = int(input("Enter number of reps: "))
                load = input("Enter load: ")
                exercise.add_set(reps, load)
            else:
                print("Exercise not found. Add it to the list.")
        elif choice == '3':
            tracker.show_all_exercises()
        elif choice == '4':
            tracker.save_to_file('exercises.json')
            print("Exercises saved. Exiting.")
            break
        else:
            print("Not a valid option. Try again.")


if __name__ == "__main__":
    main()
