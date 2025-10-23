from app import app, db
from models import Doctor

with app.app_context():
    db.drop_all()
    db.create_all()
    doctors = [
        Doctor(name="Dr. Rao", specialty="General", phone="9991112221"),
        Doctor(name="Dr. Priya", specialty="Surgery", phone="9991112222"),
        Doctor(name="Dr. Meena", specialty="Dermatology", phone="9991112223"),
        Doctor(name="Dr. Kiran", specialty="Neurology", phone="9991112224")
    ]
    db.session.add_all(doctors)
    db.session.commit()
    print("✅ Database initialized with sample doctors.")
