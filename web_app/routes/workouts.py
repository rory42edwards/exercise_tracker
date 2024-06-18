from flask import Blueprint, request, redirect, url_for, session
from datetime import datetime
from exercise_tracker import tracker


bp = Blueprint('workouts', __name__)


@bp.route('/set_date', methods=['POST'])
def set_date():
    date = request.form['date']
    session['date'] = date
    return redirect(url_for('main.index'))


@bp.route('/add_workout', methods=['POST'])
def add_workout():
    date_string = session.get('date')
    date = datetime.strptime(date_string, "%Y-%m-%y")
    if not date:
        return ("Date not set. Please set the date.")
    tracker.add_workout(date)
    return redirect(url_for('main.index'))


@bp.route('/save_workouts', methods=['POST'])
def save_workouts():
    tracker.save_to_file('test.json')
    return redirect(url_for('main.index'))


@bp.route('/load_workouts', methods=['POST'])
def load_workouts():
    try:
        session['loaded'] = True
        tracker.load_from_file('data/workouts.json')
    except FileNotFoundError:
        return "workouts.json not found!"
    return redirect(url_for('main.index'))
