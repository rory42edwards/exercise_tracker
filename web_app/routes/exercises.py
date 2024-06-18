from flask import Blueprint, request, redirect, url_for, session
from datetime import datetime
from exercise_tracker import tracker


bp = Blueprint('exercises', __name__)


@bp.route('/add_exercise', methods=['POST'])
def add_exercise():
    name = request.form['name']
    date_string = session.get('date')
    date = datetime.strptime(date_string, "%Y-%m-%y")
    workout = tracker.get_workout(date)
    workout.add_exercise(name)
    return redirect(url_for('main.index'))


@bp.route('/add_set/<name>', methods=['POST'])
def add_set(name):
    reps = int(request.form['reps'])
    load = request.form['load']
    date_string = session.get('date')
    date = datetime.strptime(date_string, "%Y-%m-%y")
    if not date:
        return "Date not set. Please set the date."
    exercise = tracker.get_exercise(name, date)
    if exercise:
        exercise.add_set(reps, load)
    else:
        return "Exercise not found. Please add it."
    return redirect(url_for('main.index'))
