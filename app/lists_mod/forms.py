from flask_wtf import FlaskForm
from wtforms import StringField,TextField
from wtforms.validators import DataRequired
from ..models import ListsItems

class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])