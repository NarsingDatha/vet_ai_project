from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CaseForm(FlaskForm):
    owner_name = StringField('Owner Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    pet_name = StringField('Pet Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    symptoms = TextAreaField('Describe Symptoms', validators=[DataRequired()])
    submit = SubmitField('Submit Case')
