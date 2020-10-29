from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from datetime import date

class AddEventForm(Form):
    name = StringField('name', [validators.Length(min=2, max=50)])
    date = DateField('date', format='%d/%m/%Y')