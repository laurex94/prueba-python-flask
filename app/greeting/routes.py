from flask import jsonify, request, abort
from app.greeting import bp
from app.extensions import db
from app.models.greeting import Greeting
from datetime import datetime

@bp.route('/', methods=['GET'])
def get_greetings():
    queries = Greeting.query.all()
    
    greeting_list = [{'id': query.id, 'mensaje': query.message} for query in queries]
    if not greeting_list:
        greeting_list.append({'mensaje': 'No hay saludos en la base de datos'})
    
    return jsonify({'result': greeting_list})

@bp.route('/', methods=['POST'])
def create_greeting():
    if not request.json or 'mensaje' not in request.json or not isinstance(request.json['mensaje'], str):
        abort(400)  # Bad request if the request is not JSON, missing 'mensaje', or 'mensaje' is not a string

    try:
        new_greeting = Greeting(message=request.json['mensaje'])
        db.session.add(new_greeting)
        db.session.commit()
        return jsonify({'result': 'Saludo creado correctamente', 'id': new_greeting.id, 'mensaje': new_greeting.message})
    except Exception as e:
        db.session.rollback()
        abort(500)  # Server error if something went wrong while creating the greeting

@bp.route('/<int:id>', methods=['GET'])
def get_greeting(id):
    if id < 0:
        abort(400)  # Bad request if the ID is not valid

    query = Greeting.query.get(id)
    if query is None:
        abort(404)  # Not found if the greeting with the provided ID does not exist
    
    return jsonify({'id': query.id, 'mensaje': query.message})

@bp.route('/content/<content>', methods=['GET'])
def get_greetings_by_content(content):
    queries = Greeting.query.filter(Greeting.message.ilike(f'%{content}%')).all()

    greeting_list = [{'id': query.id, 'mensaje': query.message} for query in queries]
    if not greeting_list:
        greeting_list.append({'mensaje': f"No se encontraron saludos con el contenido '{content}'"})
    
    return jsonify({'result': greeting_list})

@bp.route('/created_after/<date>', methods=['GET'])
def get_greetings_created_after(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')  # Convert date string to datetime object
    except ValueError:
        abort(400)  # Bad request if the date format is incorrect

    queries = Greeting.query.filter(Greeting.created_at > date_obj).all()

    greeting_list = [{'id': query.id, 'mensaje': query.message} for query in queries]
    if not greeting_list:
        greeting_list.append({'mensaje': f"No hay saludos creados después de la fecha '{date}'"})
    
    return jsonify({'result': greeting_list})
