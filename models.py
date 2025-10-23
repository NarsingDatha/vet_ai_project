from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(50))
    age = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    owner = db.relationship('Owner', backref=db.backref('pets', lazy=True))

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialty = db.Column(db.String(120), default='General')
    phone = db.Column(db.String(50))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    pet = db.relationship('Pet', backref=db.backref('appointments', lazy=True))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    owner = db.relationship('Owner')
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=True)
    doctor = db.relationship('Doctor')
    symptoms = db.Column(db.Text)
    predicted_disease = db.Column(db.String(200))
    severity = db.Column(db.String(20), default='low')
    status = db.Column(db.String(50), default='submitted')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(20))
    user_id = db.Column(db.Integer)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AmbulanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
    appointment = db.relationship('Appointment')
    status = db.Column(db.String(50), default='requested')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
