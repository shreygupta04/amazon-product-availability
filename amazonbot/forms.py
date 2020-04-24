from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Amazon Search', validators=[DataRequired()])
    submit = SubmitField('Search')
