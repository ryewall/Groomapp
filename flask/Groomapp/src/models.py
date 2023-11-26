import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.BigInteger, unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Dog(db.Model):
    __tablename__ = 'dogs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Numeric, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    breed = db.Column(db.String(128))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.Time, nullable=False )
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id'), nullable=False)

    def serialize(self):
        return {
            'appointment id': self.id,
            'appointment date': self.app_date,
            'dog id': self.dog_id
       }
    
class Service(db.Model):
    __tablename__ = 'services'
    type = db.Column(db.String(128), primary_key=True)
    length = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

appointments_services = db.Table(
    'appointments_services',
    db.Column(
        'appointment_id', db.Integer,
        db.ForeignKey('appointments.id'),
        primary_key=True
    ),

    db.Column(
        'services_type', db.String(128),
        db.ForeignKey('services.type'),
        primary_key=True
    )
)