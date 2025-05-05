from db.db_local import SessionLocal
from db.models import Workout, Exercise, Set
from sqlalchemy.orm import joinedload
from PySide6.QtWidgets import QTableWidget


def get_workouts_between_dates(start_date: str, end_date: str) -> list[Workout]:
    session = SessionLocal()

    try:
        return (
                session.query(Workout)
                .options(joinedload(Workout.exercises).joinedload(Exercise.sets))
                .filter(Workout.date >= start_date, Workout.date <= end_date)
                .order_by(Workout.date.asc())
                .all()
        )
    finally:
        session.close()


def get_all_exercise_names() -> list[str]:
    session = SessionLocal()
    try:
        results = session.query(Exercise.name).distinct().all()
        return [r[0] for r in results]
    finally:
        session.close()


def get_exercises_for_workout(workout_id: int) -> list[str]:
    session = SessionLocal()
    try:
        exercises = (
                session.query(Exercise)
                .options(joinedload(Exercise.sets))
                .filter(Exercise.workout_id == workout_id)
                .order_by(Exercise.exercise_order.asc())
                .all()
        )

        return exercises

    finally:
        session.close()


def get_sets_for_exercise_on_date(exercise_name: str, workout_date: str) -> list[Set]:
    session = SessionLocal()
    try:
        sets = (
                session.query(Set)
                .join(Set.exercise)
                .join(Exercise.workout)
                .filter(
                    Workout.date == workout_date,
                    Exercise.name == exercise_name
                )
                .order_by(Set.set_order.asc())
                .all()
        )
        return sets
    finally:
        session.close()


def get_workout_by_id(workout_id: int) -> Workout:
    session = SessionLocal()
    try:
        workout = session.query(Workout)\
                  .options(
                    joinedload(Workout.exercises).joinedload(Exercise.sets)
                   )\
                  .filter(Workout.id == workout_id)\
                  .first()
        return workout
    finally:
        session.close()


def update_workout_from_table(workout_id: int, tablewidget: QTableWidget) -> bool:
    session = SessionLocal()
    try:
        workout = session.query(Workout).filter(Workout.id == workout_id).first()
        if not workout:
            return False

        exercises = sorted(workout.exercises, key=lambda e: e.exercise_order)

        for row_index in range(tablewidget.rowCount()):
            if row_index >= len(exercises):
                continue

            exercise_obj = exercises[row_index]

            exercise_obj.exercise_name = tablewidget.item(row_index, 0).text()
            for s in exercises.sets:
                s.reps = int(tablewidget.item(row_index, 1).text())
                s.load = float(tablewidget.item(row_index, 2).text())
                s.rpe = int(tablewidget.item(row_index, 3).text())

        session.commit()
        return True

    except Exception as e:
        session.rollback()
        print(f"Error updating workout: {e}")
        return False

    finally:
        session.close()


def delete_workout_by_id(workout_id: int) -> bool:
    session = SessionLocal()
    try:
        workout = session.query(Workout)\
                  .filter(Workout.id == workout_id)\
                  .first()
        if workout:
            session.delete(workout)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        session.rollback()
        print(f"Error deleting workout: {e}")
        return False
    finally:
        session.close()
