from flask import Blueprint, request, redirect, url_for, g
from datetime import datetime
from exercise_tracker import tracker


bp = Blueprint('workouts', __name__)


def load_tracker():
    if 'tracker' not in g:
        tracker.load_from_file('data/workouts.json')
        g.tracker = tracker


@bp.before_request
def before_request():
    load_tracker()


@bp.route('/add_workout', methods=['POST'])
def add_workout():
    date_string = request.form['date']
    date = datetime.strptime(date_string, "%Y-%m-%d")
    if not date:
        return ("Date not set. Please set the date.")
    g.tracker.add_workout(date)
    g.tracker.save_to_file('data/workouts.json')
    return redirect(url_for('main.index'))
