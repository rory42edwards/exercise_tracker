from db.db_local import SessionLocal
from db.models import Workout, Set

session = SessionLocal()

# Get all workouts
workouts = session.query(Workout).all()
print(f"Total workouts: {len(workouts)}")

for workout in workouts:
    print(f"\n📅 {workout.date} - {workout.title or 'No title'}")
    for e in workout.exercises:
        print(f"  - {e.name}")

session.close()
