from flask import Flask
from flask_wtf import FlaskForm
from wtforms import TextField,StringField,validators
from wtforms.validators import DataRequired,Email,EqualTo,Length
from ..models import User

class Signupform(FlaskForm):
 first_name=TextField('first_name',validators=[DataRequired(),Length(min=1,max=30)])
 last_name=TextField('last_name',validators=[DataRequired(),Length(min=1,max=30)])
 email=StringField('email',validators=[DataRequired(),Email(),Length(min=6,max=60)])
 password=StringField('password',validators=[DataRequired(),Length(min=8,max=60)])
 # repeat_password=StringField('repeat_password',validators=[DataRequired(),EqualTo('password')])
 
 def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValueError('Email is already in use.')

class Loginform(FlaskForm):
 email=StringField('Email',validators=[DataRequired(),Email(),Length(min=6,max=60)])
 password=StringField('password',validators=[DataRequired(),Length(min=8,max=60)])
 