# 🐾 Vet AI - Smart Pet Diagnosis System

## Overview
Vet AI is an intelligent web application designed to assist pet owners and veterinarians by predicting possible diseases in pets based on the symptoms described by the user. The system analyzes input symptoms using an AI model, predicts the disease, estimates severity, and assigns an available veterinarian in real-time.

This project is implemented using Python, Flask, and machine learning techniques to provide an easy-to-use platform for pet healthcare.

---

## Features

- **User-Friendly Web Interface:** Simple form to submit pet symptoms and owner details.
- **AI-Powered Diagnosis:** Automatically predicts possible diseases using Natural Language Processing (NLP).
- **Severity Assessment:** Assigns severity level (low, medium, high) based on disease type.
- **Doctor Assignment:** Assigns an available veterinarian based on the disease.
- **Data Persistence:** Stores owner, pet, and doctor information in a SQLite database.
- **Expandable:** Can easily add more symptoms, diseases, and doctors.

---

## Technologies Used

- **Backend & Frameworks:**
  - Python 3.10
  - Flask (Web Framework)
  - Flask-WTF (Form Handling)
  - Flask-SQLAlchemy (Database ORM)
  - SQLite (Database)

- **Machine Learning & Data Processing:**
  - scikit-learn (Text classification and modeling)
  - pandas, numpy (Data handling)
  - joblib (Model serialization)

- **Frontend:**
  - HTML5 / CSS3
  - Flask Templates (Jinja2)

- **Other Utilities:**
  - email_validator (Form validation)
  - dotenv (Environment variable management)

---

## AI Model Details

- **Model Type:** Text classification using Logistic Regression.
- **Input:** Pet symptoms described as free text.
- **Preprocessing:** TF-IDF vectorization with n-grams (1,2).
- **Training Data:** Sample dataset of symptom-disease pairs (`data/sample_cases.csv`).
- **Output:** Predicted disease and corresponding severity.
- **Model Serialization:** Saved as `model_pipeline.pkl` using `joblib`.

---

## Project Structure



vet_ai_project/
│
├─ app.py # Main Flask application
├─ train_model.py # Script to train disease prediction model
├─ init_db.py # Initialize database and sample doctors
├─ models.py # SQLAlchemy models for Owner, Pet, Doctor
├─ forms.py # Flask-WTF forms
├─ model_pipeline.pkl # Trained AI model
├─ clinic.db # SQLite database file
├─ requirements.txt # Project dependencies
├─ data/
│ └─ sample_cases.csv # Sample dataset for training
├─ templates/
│ └─ index.html # Main HTML template for input form
└─ static/ # Static files (CSS, JS, images)


---

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd vet_ai_project

    Create virtual environment and activate

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Train the AI model

python3 train_model.py

Initialize the database with sample doctors

python3 init_db.py

Run the Flask application

    python3 app.py

    Open your browser at http://127.0.0.1:5000.

Usage

    Fill out the Owner Details: Name, Phone, Email.

    Enter Pet Details: Name, Species, Age.

    Describe Pet Symptoms in the text box.

    Click Submit Case.

    The system will:

        Predict the disease

        Determine severity

        Assign an available veterinarian

    View results immediately on the same page.

Future Enhancements

    Add real-time notifications for doctors.

    Integrate with SMS/email alerts for appointment updates.

    Extend disease database with more complex symptoms.

    Incorporate multi-language support for owners.

    Integrate with ambulance and emergency services for high-severity cases.

Author

Your Name:
Email:

GitHub:

