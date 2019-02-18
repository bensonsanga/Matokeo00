from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class SearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year = SelectField(u'Year', choices=[('2017', '2017'), ('2018', '2018'), ('2016', '2016'), ('2015', '2015')])
    exam = SelectField(u'Exam', choices=[('csee', 'CSEE'), ('acsee', 'ACSEE')])
    student_number = TextAreaField('Student Number', validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField('Search')
