from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    format = StringField('format',validators=[DataRequired()])
    num_page = StringField('pages',validators=[DataRequired()])
    submit =SubmitField('update')

class CreateBookForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    author = StringField('author',validators=[DataRequired()])
    avg_rating = FloatField('rating',validators=[DataRequired()])
    format = StringField('format',validators=[DataRequired()])
    img_url = StringField('image',validators=[DataRequired()])
    num_page = IntegerField('pages',validators=[DataRequired()])
    pub_id = IntegerField('publisherid',validators=[DataRequired()])
    submit = SubmitField('Create')