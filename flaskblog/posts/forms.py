from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class SearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year = SelectField(u'Year', choices=[('2017', '2017'), ('2018', '2018'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2008', '2008'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001')])
    exam = SelectField(u'Exam', choices=[('csee', 'CSEE'), ('acsee', 'ACSEE'), ('ftna', 'FTNA'), ('ftsee', 'FTSEE'), ('heslb', 'HESLB'), ('psle', 'PSLE'), ('qt', 'QT'), ('sfna', 'SFNA')])
    student_number = TextAreaField('Student Number', validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField('Search')
