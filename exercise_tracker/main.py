from datetime import datetime
import csv
from exercise_tracker import ExerciseTracker


def manual_input(rows):
    date_string = input("Enter date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%y")
    notes = input("Any significant notes to add?\
 eg injuries, unusual focus of the session, etc.: ")
    add_another_exercise = True
    counter = 1
    while add_another_exercise:
        exercise = input("Enter exercise: ")
        sets = input("Enter sets: ")
        reps = input("Enter reps: ")
        weight = input("Enter weight: ")
        row = [date, exercise, sets, reps, weight]
        if counter == 1:
            row.append(notes)
        rows.append(row)
        yesno = input("Add another exercise? [y/n] ")
        if yesno.lower() == "y":
            add_another_exercise = True
            counter += 1
        else:
            add_another_exercise = False
    return rows


def main():
    """
    rows = []
    with open("exercise.csv", 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # extract field names from first row
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

    print(fields)
    for row in rows:
        print(row)

    # rows.append(["joe", "mama"])
    rows = manual_input(rows)
    for row in rows:
        print(row)

    with open("exercise.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    """
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
                exercise.add_set(reps)
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
