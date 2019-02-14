from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class SearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = TextAreaField('Student Number', validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField('Search')
