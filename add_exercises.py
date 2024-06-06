from datetime import datetime
import csv


def manual_input(rows):
    date_string = input("Enter date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%y")
    add_another_exercise = True
    while add_another_exercise:
        exercise = input("Enter exercise: ")
        sets = input("Enter sets: ")
        reps = input("Enter reps: ")
        weight = input("Enter weight: ")
        row = [date, exercise, sets, reps, weight]
        rows.append(row)
        yesno = input("Add another exercise? [y/n] ")
        if yesno.lower() == "y":
            add_another_exercise = True
        else:
            add_another_exercise = False
    return rows


def main():
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


if __name__ == "__main__":
    main()
