from flask import Blueprint, g, request
from flask.json import jsonify
from exercise_analysis import analyser
from exercise_tracker import tracker
from web_app.models import Movement, Tag


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


@bp.route('/api/exercise_load/', methods=['GET'])
def get_exercise_load():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    movement = g.analyser.get_movement(name)
    if not movement:
        return jsonify({'error': f"Movement: {name} not found!"}), 404
    data = g.analyser.get_load_data(movement)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': "Failed to generate plot"}), 500


@bp.route('/api/exercise_load_volume/', methods=['GET'])
def get_exercise_load_volume():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    movement = g.analyser.get_movement(name)
    if not movement:
        return jsonify({'error': f"Movement: {name} not found!"}), 404
    data = g.analyser.get_load_volume_data(movement)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': "Failed to generate plot"}), 500


@bp.route('/api/get_data', methods=['GET'])
def get_data():
    workouts = [workout.to_dict() for workout in g.tracker.workouts]
    return jsonify(workouts)


@bp.route('/api/get_movements', methods=['GET'])
def get_movements():
    movements = Movement.query.all()
    result = [{'id': movement.id, 'name': movement.name}
              for movement in movements]
    return jsonify(result), 200


@bp.route('/api/get_tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    result = [{'id': tag.id, 'name': tag.name} for tag in tags]
    return jsonify(result), 200


@bp.route('/api/get_combined_data', methods=['GET'])
def get_combined_data():
    movements = Movement.query.all()

    results = []
    for movement in movements:
        tags_dict = {mt.tag.name: mt.value for mt in movement.movement_tags}
        results.append({
            'id': movement.id,
            'name': movement.name,
            'tags': tags_dict
        })

    return jsonify(results), 200


@bp.route('/api/get_prog_overload', methods=['GET'])
def get_exercise_prog_overload():
    """
    Gets information about progressive overload of an exercise in reps or load
    """
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    movement = g.analyser.get_movement(name)
    if not movement:
        return jsonify({'error': f"Movement: {name} not found!"}), 404
    data = g.analyser.get_prog_overload(movement)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': "Failed to generate plot"}), 500
