import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Workout, Superset, Exercise, Set

# Set up DB
engine = create_engine("sqlite:///data/repdojo.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if not exist
Base.metadata.create_all(engine)

# Load JSON
with open("data/workouts.json", "r") as f:
    data = json.load(f)

# Parse + insert
for workout in data:
    w = Workout(
        date=datetime.strptime(workout["date"], "%Y-%m-%dT%H:%M:%S").date(),
        title=workout.get("title", ""),
        notes=workout.get("notes", "")
    )
    session.add(w)
    session.flush()  # Get the workout.id

    supersets = {}
    for i, exercise in enumerate(workout["exercises"]):
        label = exercise.get("superset")
        if label:
            if label not in supersets:
                s = Superset(workout_id=w.id)
                session.add(s)
                session.flush()
                supersets[label] = s
            superset_id = supersets[label].id
        else:
            superset_id = None

        e = Exercise(
            workout_id=w.id,
            name=exercise['name'],
            exercise_order=i,
            superset_id=superset_id
        )
        session.add(e)
        session.flush()  # get the exercise id
        for idx, s in enumerate(exercise["sets"]):
            set_obj = Set(
                    exercise_id=e.id,
                    reps=s["reps"],
                    load=s["load"],
                    set_order=idx
            )
            session.add(set_obj)

session.commit()
print(f"Migration complete. Imported {len(data)} workouts.")
