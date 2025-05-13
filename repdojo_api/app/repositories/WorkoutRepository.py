from app.db.models import Workout, Exercise, Set
from app.db.db_local import SessionLocal
from app.schemas.workout import SaveWorkout
from sqlalchemy.orm import joinedload
from datetime import date, datetime


class WorkoutRepository:

    @staticmethod
    def get_by_id(workout_id: int) -> Workout:
        """Returns a Workout database object from an id.

        Args:
            workout_id (int): The workout id of a Workout in the database.

        Returns:
            Workout: A Workout database object.
        """
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

    @staticmethod
    def delete(workout_id: int) -> bool:
        session = SessionLocal()
        try:
            workout = session.query(Workout).filter(Workout.id == workout_id).first()
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

    @staticmethod
    def list_between_dates(start_date: date, end_date: date) -> list[Workout]:
        if not isinstance(start_date, date) or not isinstance(end_date, date):
            raise TypeError(f"Input dates must be datetime.date objects.\nCurrently types are: start_date {type(start_date)}, end_date {type(end_date)}")
        session = SessionLocal()
        try:
            workouts = session.query(Workout)\
                .filter(Workout.date >= start_date, Workout.date <= end_date)\
                .order_by(Workout.date.desc())\
                .all()
            return workouts
        finally:
            session.close()

    @staticmethod
    def save_workout(save_workout_data: SaveWorkout) -> dict:
        session = SessionLocal()
        try:
            if save_workout_data is None:
                raise ValueError("No data received or invalid JSON")
            workout_data = save_workout_data.workout
            date_str = workout_data.date
            title = workout_data.title
            notes = workout_data.notes
            workout = Workout(
                    date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                    title=title,
                    notes=notes
            )
            session.add(workout)
            session.flush()

            for i, exercise in enumerate(workout_data.exercises):
                exercise_obj = Exercise(
                        workout_id=workout.id,
                        name=exercise.name,
                        exercise_order=i
                )
                session.add(exercise_obj)
                session.flush()
                for idx, s in enumerate(exercise.sets):
                    set_obj = Set(
                            exercise_id=exercise_obj.id,
                            reps=s.reps,
                            load=s.load,
                            rpe=s.rpe,
                            set_order=idx
                    )
                    session.add(set_obj)

            session.commit()
            return {"success": True}, 200

        except Exception as e:
            print(f"Error in save_workout: {e}")
            session.rollback()
            return {"success": False, "error": str(e)}, 500

        finally:
            session.close()
