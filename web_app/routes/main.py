from flask import Blueprint, render_template, session, g, jsonify, request
from exercise_tracker import tracker
from exercise_tracker.workout import Workout
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
def trackerr():
    workouts = g.tracker.workouts_by_date()
    date = session.get('date')
    loaded = session.get('loaded', False)
    return render_template('tracker.html',
                           date=date,
                           workouts=workouts,
                           loaded=loaded)


@bp.route('/analysis')
def analysis():
    movements = g.analyser.movements
    return render_template('analysis.html',
                           movements=movements)


@bp.route('/dbmodels')
def dbmodels():
    return render_template('dbmodels.html')


@bp.route('/save', methods=['POST'])
def save_data():
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
