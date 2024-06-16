from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
from exercise_tracker.exercise import Exercise
from exercise_tracker.exercise_tracker import ExerciseTracker
from datetime import datetime
import json

app = Flask(__name__)

# Configure session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'bj69420'
Session(app)

tracker = ExerciseTracker()


@app.route('/')
def index():
    exercises = tracker.exercises
    date = session.get('date')
    return render_template('index.html', date=date, exercises=exercises)


@app.route('/set_date', methods=['POST'])
def set_date():
    date = request.form['date']
    session['date'] = date
    return redirect(url_for('index'))


@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    name = request.form['name']
    # date = session.get('date')
    date_string = session.get('date')
    date = datetime.strptime(date_string, "%Y-%m-%y")
    if not date:
        return ("Date not set. Please set the date.")
    # date_string = request.form['date']
    # date = datetime.strptime(date_string, "%d/%m/%y")
    tracker.add_exercise(name, date)
    return redirect(url_for('index'))


@app.route('/add_set/<name>', methods=['POST'])
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
    return redirect(url_for('index'))


@app.route('/save_exercises', methods=['POST'])
def save_exercises():
    with open("test.json", 'w') as f:
        json.dump([exercise.to_dict()
                   for exercise in tracker.exercises], f, indent=4)
    return redirect(url_for('index'))


@app.route('/load_exercises', methods=['POST'])
def load_exercises():
    try:
        session['loaded'] = True
        with open("data/exercises.json", 'r') as f:
            exercises_data = json.load(f)
            tracker.exercises =\
                [Exercise.from_dict(data) for data in exercises_data]
    except FileNotFoundError:
        return "exercises.json not found!"
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
