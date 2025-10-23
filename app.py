import os
from flask import Flask, render_template, redirect, url_for, flash
from forms import CaseForm
from models import db, Owner, Pet, Doctor, Appointment, Notification, AmbulanceRequest
import joblib

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'demo_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'clinic.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

model = joblib.load('model_pipeline.pkl')

SEVERITY_MAP = {
    'Fracture': 'high',
    'Trauma': 'high',
    'Neurological Emergency': 'high',
    'Internal Bleeding': 'high',
    'Respiratory Infection': 'medium',
    'Gastroenteritis': 'medium',
    'Dermatitis': 'low',
    'Indigestion': 'low'
}

SPECIALTY_MAP = {
    'Fracture': 'Surgery',
    'Trauma': 'Surgery',
    'Orthopedic Injury': 'Surgery',
    'Neurological Emergency': 'Neurology',
    'Dermatitis': 'Dermatology',
    'Gastroenteritis': 'General',
    'Respiratory Infection': 'General'
}

def notify(user_type, user_id, message):
    n = Notification(user_type=user_type, user_id=user_id, message=message)
    db.session.add(n)
    db.session.commit()
    print(f"NOTIFY: {user_type} {user_id} -> {message}")

def assign_doctor(specialty):
    doc = Doctor.query.filter(Doctor.specialty.ilike(f"%{specialty}%")).first()
    return doc or Doctor.query.first()

@app.route('/', methods=['GET','POST'])
def index():
    form = CaseForm()
    if form.validate_on_submit():
        owner = Owner(name=form.owner_name.data, phone=form.phone.data, email=form.email.data)
        db.session.add(owner); db.session.commit()
        pet = Pet(name=form.pet_name.data, species=form.species.data, age=form.age.data, owner=owner)
        db.session.add(pet); db.session.commit()

        symptoms = form.symptoms.data
        disease = model.predict([symptoms])[0]
        severity = SEVERITY_MAP.get(disease, 'low')
        specialty = SPECIALTY_MAP.get(disease, 'General')

        appt = Appointment(pet=pet, owner=owner, symptoms=symptoms,
                           predicted_disease=disease, severity=severity)
        db.session.add(appt); db.session.commit()

        doc = assign_doctor(specialty)
        if doc:
            appt.doctor = doc
            appt.status = 'assigned'
            db.session.commit()
            notify('owner', owner.id, f"Doctor {doc.name} assigned for {disease}")
            notify('doctor', doc.id, f"New appointment for {pet.name} - {disease}")

        if severity == 'high':
            amb = AmbulanceRequest(appointment=appt)
            db.session.add(amb)
            db.session.commit()
            notify('owner', owner.id, "Ambulance dispatched for emergency case!")

        flash(f"Disease: {disease} (Severity: {severity}) - Doctor assigned: {doc.name if doc else 'None'}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)
