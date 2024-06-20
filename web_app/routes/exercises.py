from flask import Blueprint, request, redirect, url_for
from datetime import datetime
from exercise_tracker import tracker


bp = Blueprint('exercises', __name__)


@bp.route('/add_exercise/<date>', methods=['POST'])
def add_exercise(date):
    name = request.form['name']
    date_dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    workout = tracker.get_workout(date_dt)
    if not workout:
        return f"No workout found for date: {date}"
    workout.add_exercise(name)
    return redirect(url_for('main.index'))


@bp.route('/add_set/<date>/<name>', methods=['POST'])
def add_set(date, name):
    reps = int(request.form['reps'])
    load = request.form['load']
    date_dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    if not date:
        return "Date not set. Please set the date."
    workout = tracker.get_workout(date_dt)
    if not workout:
        return f"No workout found for date: {date}"
    exercise = workout.get_exercise(name)
    if not exercise:
        return "Exercise not found. Please add it."
    exercise.add_set(reps, load)
    return redirect(url_for('main.index'))
