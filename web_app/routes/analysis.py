from flask import Blueprint, g, request
from flask.json import jsonify
from exercise_analysis import analyser
from exercise_tracker import tracker


bp = Blueprint('analysis', __name__)


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


# @bp.route('/plot_movement_load/<name>', methods=['POST'])
# def plot_movement_load(name):
@bp.route('/api/exercise_data/', methods=['GET'])
def get_exercise_data():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    movement = g.analyser.get_movement(name)
    if not movement:
        # return f"Movement: {name} not found!"
        return jsonify({'error': f"Movement: {name} not found!"}), 404
    data = g.analyser.get_plot_data(movement)
    if data:
        print(data)
        # return send_file(filepath, mimetype='image/png')
        return jsonify(data)
    else:
        return jsonify({'error': "Failed to generate plot"}), 500
        # return "Failed to generate plot", 500
