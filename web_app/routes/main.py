from flask import Blueprint, render_template, session, g, jsonify, request
from exercise_tracker import tracker
from exercise_tracker.workout import Workout
from exercise_tracker.exercise import Exercise
from exercise_analysis import analyser


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
    data = request.get_json()
    if data is None:
        raise ValueError("No data received or invalid JSON")
    date_str = data['date']
    workout = Workout(date_str)
    workout.exercises = [Exercise.from_dict(data_entry) for data_entry in data['exercises']]
    g.tracker.workouts.append(workout)
    print(f"saving workout: {workout} to file")
    g.tracker.save_to_file('data/workouts.json')
    return jsonify({'success': True})
