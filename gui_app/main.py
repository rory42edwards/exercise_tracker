import sys
import os
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QPushButton
from PySide6.QtCore import QDir, QFile, QTextStream, Qt
from PySide6.QtGui import QIcon
import pyqtgraph as pg
from db.db_local import SessionLocal
from db.models import Exercise, Workout
from datetime import date
from gui_app.utils.dateaxis import DateAxis
from gui_app.utils.colour_plot_widgets import (
        set_plot_widget_dark, set_plot_widget_light)
from gui_app.repositories.SetRepository import SetRepository
from gui_app.repositories.ExerciseRepository import ExerciseRepository
from gui_app.repositories.WorkoutRepository import WorkoutRepository
from gui_app.src.ui.edit_workout_dialogue import EditWorkoutDialog

uiclass, baseclass = pg.Qt.loadUiType("gui_app/src/ui/lifting_dashboard.ui")
session = SessionLocal()

if hasattr(sys, '_MEIPASS'):
    # running in PyInstaller bundle
    base_path = sys._MEIPASS
else:
    # running in dev
    base_path = os.path.abspath("./gui_app/")
QDir.addSearchPath('images', os.path.join(base_path, 'assets', 'images'))
QDir.addSearchPath('styles', os.path.join(base_path, 'assets', 'styles'))


class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if sys.platform == "linux":
            self.setWindowIcon(QIcon("images:repdojo_clean_symbol_128x128.png"))
        elif sys.platform == "win32":
            self.setWindowIcon(QIcon("images:repdojo_icon.ico"))
        else:
            print(f"Running on {sys.platform}")

        # set up graph widget
        self.graphWidget = pg.PlotWidget(
                axisItems={'bottom': DateAxis(orientation='bottom')}
                )
        self.graphHBoxLayout.addWidget(self.graphWidget)

        # Set initial theme and connect the dark mode toggle
        self.set_light_mode()
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setChecked(False)
        self.actionDark_Mode.triggered.connect(self.toggle_dark_mode)

        self.plot_total_sets("1001-01-01")

        # connect buttons to backend functions
        self.filterButton.clicked.connect(self.filter_workouts_by_date)

    def plot_total_sets(self, start_date: str, end_date: date=date.today()):
        start_date: date = date.fromisoformat(start_date)
        workouts: list[Workout] = WorkoutRepository.list_between_dates(start_date, end_date)

        dates = []
        sets = []
        for workout in workouts:
            nsets = SetRepository.get_total_sets(workout.date)
            dates.append(workout.date)
            sets.append(nsets)

        ordinals = [d.toordinal() for d in dates]

        plot = self.graphWidget.getPlotItem()
        plot.setLabel('left', 'Total Sets')
        plot.setLabel('bottom', 'Date')

        self.graphWidget.plot(ordinals, sets)

    def set_dark_mode(self):
        set_plot_widget_dark(self.graphWidget)
        self.dark_mode = True
        file = QFile("styles:repdojo_dark.qss")
        if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

    def set_light_mode(self):
        set_plot_widget_light(self.graphWidget)
        self.dark_mode = False
        file = QFile("styles:repdojo_light.qss")
        if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

    def toggle_dark_mode(self):
        if self.actionDark_Mode.isChecked():
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def filter_workouts_by_date(self):
        from_date = self.fromDateEdit.date().toPython()
        to_date = self.toDateEdit.date().toPython()
        self.load_workouts(from_date, to_date)

    def load_workouts(self, start_date=date.fromisoformat("2001-01-01"), end_date=date.today()):
        workouts: list[Workout] = WorkoutRepository.list_between_dates(start_date, end_date)

        # set up table
        self.workoutTableWidget.clear()
        self.workoutTableWidget.setRowCount(len(workouts))
        self.workoutTableWidget.setColumnCount(3)
        for index, workout in enumerate(workouts):
            exercises: list[Exercise] = \
                    ExerciseRepository.get_exercises(workout.id)
            self.workoutTableWidget.setItem(index, 0,
                    self.make_cell(f"{workout.date}: {len(exercises)} exercises", Id=workout.id)
            )
            self.workoutTableWidget.setItem(index, 1,
                    self.make_cell(workout.title, Id=workout.id)
            )
            for exercise in exercises:
                sets = SetRepository.get_sets_for_exercise_on_date(
                        exercise.name,
                        workout.date)
            # add and connect edit workout button
            editWorkoutButton = QPushButton("Edit Workout")
            editWorkoutButton.setProperty("workout_id", workout.id)
            editWorkoutButton.clicked.connect(self.open_edit_workout_dialog)
            self.workoutTableWidget.setCellWidget(index, 2, editWorkoutButton)

    def make_cell(self, text, bold=False, Id=None):
        item = QTableWidgetItem(text)
        font = item.font()
        font.setBold(bold)
        item.setFont(font)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        item.setTextAlignment(Qt.AlignCenter)
        if id:
            item.setData(Qt.UserRole, id)
        return item

    def open_edit_workout_dialog(self):
        button = self.sender()
        if not button:
            print("nope")
            return
        workout_id = button.property("workout_id")
        if workout_id is None:
            print("Button has no workout ID!")
            return
        dialog = EditWorkoutDialog(workout_id)
        if dialog.exec():
            self.load_workouts()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
