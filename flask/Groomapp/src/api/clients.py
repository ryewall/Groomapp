from flask import Blueprint, jsonify, abort, request
from ..models import Client, db, Appointment

bp = Blueprint('clients', __name__, url_prefix='/clients')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    clients = Client.query.all() # ORM performs SELECT query
    result = []
    for c in clients:
        result.append(c.serialize()) # build list of users as dictionaries
    return jsonify(result) # return JSON response