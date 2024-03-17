from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    bedrooms = StringField('bedrooms', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    price = StringField('price', validators=[InputRequired()])
    type = SelectField('type', choices= [('house','House'), ('apartment','Apartment')], validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    photo = FileField('Photo', validators = [
        FileRequired(),
        FileAllowed(['jpg','png'],'Only Images are Allowed')
    ])

