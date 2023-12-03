from flask import Blueprint, jsonify, abort, request
from ..models import Client, db, Appointment

bp = Blueprint('clients', __name__, url_prefix='/clients')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    clients = Client.query.all()  # ORM performs SELECT query
    result = []
    for c in clients:
        result.append(c.serialize())  # build list of users as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('', methods=['POST'])
def create():
    data = request.json

    if 'name' not in data or 'phone_number' not in data:
        abort(400, 'Name and phone_number are required.')

    new_client = Client(name=data['name'], phone_number=data['phone_number'])

    db.session.add(new_client)
    db.session.commit()

    return jsonify(new_client.serialize()), 201
