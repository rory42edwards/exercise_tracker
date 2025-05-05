from flask import Blueprint, render_template, g, jsonify, request, current_app
from exercise_tracker import tracker
# from exercise_tracker.workout import Workout
# from exercise_tracker.exercise import Exercise
from exercise_analysis import analyser
from db.models import Workout, Exercise, Set
from datetime import datetime
from sqlalchemy import desc


bp = Blueprint('main', __name__)


def load_tracker():
    if 'tracker' not in g:
        tracker.load_from_file('data/workouts.json')
        g.tracker = tracker


def load_analyser():
    if 'analyser' not in g:
        analyser.create_movements(g.tracker.workouts)
        g.analyser = analyser


@bp.before_request
def before_request():
    load_tracker()
    load_analyser()


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/history')
def history():
    session = current_app.session_local()
    workouts = g.tracker.workouts_by_date()
    date = session.get('date')
    loaded = session.get('loaded', False)
    # workouts = get_all_workouts()
    # return render_template('history.html', workouts=workouts)
    return render_template('history.html',
                           date=date,
                           workouts=workouts,
                           loaded=loaded)


@bp.route('/log_workout')
def log_workout():
    return render_template('log_workout.html')


@bp.route('/analysis')
def analysis():
    movements = [movement.to_dict() for movement in g.analyser.movements]
    return render_template('analysis.html',
                           python_movements=movements)


@bp.route('/dbmodels')
def dbmodels():
    movements = [movement.to_dict() for movement in g.analyser.movements]
    return render_template('dbmodels.html',
                           python_movements=movements)


@bp.route('/save_tracker', methods=['POST'])
def save_tracker():
    data = request.get_json()
    if data is None:
        raise ValueError("No data received or invalid JSON")
    print(data)
    g.tracker.workouts =\
        [Workout.from_dict(data_entry) for data_entry in data]
    for workout in g.tracker.workouts:
        print(workout)
    g.tracker.save_to_file('data/workouts.json')
    return jsonify({'success': True})


@bp.route('/save_workout', methods=['POST'])
def save_workout():
    session = current_app.session_local()
    data = request.get_json()
    try:
        if data is None:
            raise ValueError("No data received or invalid JSON")
        date_str = data['date']
        title = data.get("title", "")
        notes = data.get("notes", "")  # default to empty string if missing
        workout = Workout(
                date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                title=title,
                notes=notes
        )
        session.add(workout)
        session.flush()

        for i, exercise in enumerate(data['exercises']):
            exercise_obj = Exercise(
                    workout_id=workout.id,
                    name=exercise['name'],
                    exercise_order=i
            )
            session.add(exercise_obj)
            session.flush()
            for idx, s in enumerate(exercise['sets']):
                rpe = s.get('rpe', -1)  # default rpe to -1 if it doesn't exist
                set_obj = Set(
                        exercise_id=exercise_obj.id,
                        reps=s['reps'],
                        load=s['load'],
                        rpe=rpe,
                        set_order=idx
                )
                session.add(set_obj)

        session.commit()
        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print(f"Error in save_workout: {e}")
        session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        session.close()


@bp.route('/get_last_exercise_data/<exercise_name>', methods=['GET'])
def get_last_exercise_data(exercise_name: str):
    session = current_app.session_local()
    try:
        result = (
                session.query(Workout.date)
                .join(Set)
                .filter(Set.exercise_name == exercise_name)
                .order_by(desc(Workout.date))
                .first()
        )
        if result:
            return jsonify({"last_date": result.date.isoformat()}), 200
        else:
            return jsonify({"last_date": None}), 200

    except Exception as e:
        print(f"Error in get_last_exercise_data: {e}")
        session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        session.close()
