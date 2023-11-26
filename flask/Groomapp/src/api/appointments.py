from flask import Blueprint, jsonify, abort, request
from ..models import Appointment, Client, db

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    appointments = Appointment.query.all() # ORM performs SELECT query
    result = []
    for a in appointments:
        result.append(a.serialize()) # build list of appointments as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Appointment.query.get_or_404(id, "Appointment not found")
    return jsonify(a.serialize())

@bp.route('', methods=['POST'])
def create_appointment():
    if request.method == 'POST':
        # Extract data from the JSON request
        data = request.json

        # Validate and extract the required fields from the request data
        date = data.get('date')
        time = data.get('time')
        dog_id = data.get('dog_id')

        if date is None or dog_id is None:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create the appointment
        appointment = Appointment(app_date=date, app_time=time, dog_id=dog_id)

        # Add the appointment to the database
        db.session.add(appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment created successfully'}), 201



@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Appointment.query.get_or_404(id, "Appointment not found")
    try:
        db.session.delete(a) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)