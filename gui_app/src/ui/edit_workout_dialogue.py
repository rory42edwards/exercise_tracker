from PySide6.QtWidgets import (
        QVBoxLayout, QTableWidget, QPushButton, QDialog, QTableWidgetItem
)
from gui_app.utils.db_queries import (
        get_workout_by_id, update_workout_from_table, delete_workout_by_id
)
from gui_app.repositories.WorkoutRepository import WorkoutRepository
from gui_app.repositories.ExerciseRepository import ExerciseRepository
from gui_app.repositories.SetRepository import SetRepository
from db.models import Workout, Exercise, Set


class EditWorkoutDialog(QDialog):
    def __init__(self, workout_id):
        super().__init__()
        self.workout_id = workout_id
        self.setupUi()
        self.load_workout()

    def setupUi(self) -> None:
        self.layout = QVBoxLayout(self)
        self.setWindowTitle("Edit Workout")

        self.exerciseTable = QTableWidget()
        self.exerciseTable.setColumnCount(5)
        self.exerciseTable.setHorizontalHeaderLabels(["Exercise", "Reps", "Load", "RPE", "Delete"])
        self.layout.addWidget(self.exerciseTable)

        self.saveButton = QPushButton("Save Changes")
        self.deleteButton = QPushButton("Delete Workout")
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.deleteButton)

        self.saveButton.clicked.connect(self.save_changes)
        self.deleteButton.clicked.connect(self.delete_workout)

    def load_workout(self) -> None:
        workout: Workout = WorkoutRepository.get_by_id(self.workout_id)
        self.exerciseTable.setRowCount(0)
        for e in workout.exercises:
            self.create_exercise_rows(e)

    def create_exercise_rows(self, exercise: Exercise) -> None:
        for s in exercise.sets:
            self.create_set_row(s, exercise.name)
        # add empty row
        row = self.exerciseTable.rowCount()
        self.exerciseTable.insertRow(row)

    def create_set_row(self, s: Set, exercise_name: str) -> None:
        row = self.exerciseTable.rowCount()
        self.exerciseTable.insertRow(row)
        self.exerciseTable.setItem(row, 0, QTableWidgetItem(exercise_name))
        self.exerciseTable.setItem(row, 1, QTableWidgetItem(str(s.reps)))
        self.exerciseTable.setItem(row, 2, QTableWidgetItem(str(s.load)))
        self.exerciseTable.setItem(row, 3, QTableWidgetItem(str(s.rpe)))

        # Add delete button
        delete_button = QPushButton("❌")
        delete_button.setProperty("set_id", s.id)
        delete_button.clicked.connect(self.delete_set)
        self.exerciseTable.setCellWidget(row, 4, delete_button)

    def save_changes(self) -> None:
        # Read from table, update database
        update_workout_from_table(self.workout_id, self.exerciseTable)
        self.accept()

    def delete_workout(self) -> None:
        # delete_workout_by_id(self.workout_id)
        WorkoutRepository.delete(self.workout_id)
        self.accept()

    def delete_exercise(self, exercise_id: int) -> None:
        ExerciseRepository.delete(exercise_id)

    def delete_set(self) -> None:
        button = self.sender()
        set_id = button.property("set_id")
        if set_id:
            SetRepository.delete(set_id)
            self.load_workout()

    def reload_workout(self) -> None:
        ...
