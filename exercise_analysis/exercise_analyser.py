from exercise_analysis.movement import Movement
from exercise_tracker.workout import Workout
from exercise_tracker.set import Set
from datetime import datetime
from typing import Type, Union, Optional
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


class ExerciseAnalyser:
    def __init__(self):
        self.movements = []

    def create_movements(self, workouts: list['Workout']) -> None:
        # make sure self.movements is empty
        self.movements.clear()
        # create unique list of exercise names
        exercise_names: list[str] = []
        for workout in workouts:
            # print(workout)
            for exercise in workout.exercises:
                # print(exercise)
                if exercise.name not in exercise_names:
                    exercise_names.append(exercise.name.lower().strip())
        movements = [Movement(name.strip()) for name in exercise_names]

        for movement in movements:
            for workout in workouts:
                for exercise in workout.exercises:
                    if exercise.name.strip() == movement.name.strip():
                        movement.add_workout(workout.date, exercise.sets)
            self.movements.append(movement)

    def plot_exercises_per_workout(self, workouts: list[Type['Workout']]) -> None:
        dates = [workout.date for workout in workouts]
        number_of_exercises = [len(workout.exercises) for workout in workouts]

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

    def plot_load_over_time(self, movement: Movement) -> Optional[str]:
        dates = []
        highest_loads = []
        for date, sets in movement.all_sets.items():
            dates.append(date.date())
            loads = []
            for sett in sets:
                loads.append(float(sett.load))
            highest_loads.append(max(loads))
        if len(dates) != len(highest_loads):
            return None
        plt.figure()
        plt.scatter(dates, highest_loads, label=f"{movement.name} - Load")
        plt.xlabel("Date")
        plt.ylabel("Load / kg")
        plt.title(f"Load over time: {movement.name}")
        plt.xticks(rotation=45)

        static_folder = os.path.join(os.path.dirname(__file__),
                                     '..', 'static', 'images')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
        filepath = os.path.join(static_folder, f"{movement.name}_load.png")
        plt.savefig(filepath, format="png")
        plt.close()
        return filepath

    def get_load_data(self, movement: Movement) -> dict:
        dates = []
        highest_loads = []
        for date, sets in movement.all_sets.items():
            dates.append(date)
            loads = [float(sett.load) for sett in sets]
            highest_loads.append(max(loads))
        return {
                'labels': dates,
                'values': highest_loads
        }

    def plot_load_volume_over_time(self, movement: Movement) -> Optional[str]:
        dates = []
        load_volumes = []
        for date, sets in movement.all_sets.items():
            dates.append(date.date())
            load_volume: float = 0.0
            for sett in sets:
                if float(sett.load) == 0.0:  # for now, if bodyweight,just make it one and then reps are still compared
                    sett.load = 1
                load_volume += float(sett.reps) * float(sett.load)
            load_volumes.append(load_volume)
        if len(dates) != len(load_volumes):
            return None
        plt.figure()
        plt.scatter(dates, load_volumes, label=f"{movement.name} - Load-Volume")
        plt.xlabel("Date")
        plt.ylabel("Load-Volume / kg")
        plt.title(f"Load-volume over time: {movement.name}")
        plt.xticks(rotation=45)

        static_folder = os.path.join(os.path.dirname(__file__),
                                     '..', 'static', 'images')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
        filepath = os.path.join(static_folder, f"{movement.name}_load_volume.png")
        plt.savefig(filepath, format="png")
        plt.close()
        return filepath

    def get_load_volume_data(self, movement: Movement) -> dict:
        dates = []
        load_volumes = []
        for date, sets in movement.all_sets.items():
            dates.append(date)
            load_volume: float = 0.0
            for sett in sets:
                if float(sett.load) == 0.0:  # for now, if bodyweight,just make it one and then reps are still compared
                    sett.load = 1
                load_volume += float(sett.reps) * float(sett.load)
            load_volumes.append(load_volume)
        return {
                'labels': dates,
                'values': load_volumes
        }

    def get_movement(self, name: str) -> Union[Movement, None]:
        for movement in self.movements:
            if movement.name.lower() == name.lower():
                return movement
        return None

    def get_prog_overload(slef, movement: Movement) -> dict:
        """
        Returns information about changes in maximum load,
        or if that's the same, changes in reps of a movement, over time
        """
        dates: list[str] = []
        all_set_load_volumes: list[tuple] = []
        for date, sets in movement.all_sets.items():
            dates.append(date)
            loads: list[float] = []
            total_reps: int = 0
            for sett in sets:
                loads.append(sett[1])
                total_reps += sett[0]
            highest_load: float = max(loads)
            all_set_load_volumes.append((total_reps, highest_load))
        overloads: list[int] = []
        for i in range(len(all_set_load_volumes)):
            if i == 0:
                overloads.append(0)
                continue
            # check if load is bigger than previous one
            if all_set_load_volumes[i][1] > all_set_load_volumes[i-1][1]:
                overloads.append(overloads[-1]+1)
                continue
            if all_set_load_volumes[i][1] < all_set_load_volumes[i-1][1]:
                overloads.append(overloads[-1]-1)
                continue
            # if load is the same, check if reps increased or decreased
            if all_set_load_volumes[i][0] > all_set_load_volumes[i-1][0]:
                overloads.append(overloads[-1]+1)
                continue
            if all_set_load_volumes[i][0] < all_set_load_volumes[i-1][0]:
                overloads.append(overloads[-1]-1)
                continue
            # if none of the conditions above are met, no change
            # (ie same reps and load == no overloading or underloading)
            overloads.append(overloads[-1])
        return {
                'labels': dates,
                'values': overloads
        }
