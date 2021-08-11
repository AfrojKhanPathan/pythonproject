from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Length, Email,EqualTo,ValidationError
from app.auth.models import User

def email_exist(form,field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already Exists')

class RegistrationForm(FlaskForm):
    name = StringField('Whats your name',validators=[DataRequired(),Length(3,15,message='between 3 to 15 character')])
    email = StringField('enter your email',validators=[DataRequired(),Email(),email_exist])
    password = PasswordField('Password',validators=[DataRequired(),Length(5),EqualTo('comform',message= 'password must match')])
    config = PasswordField('conform ',validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email])
    password = PasswordField('password',validators=[DataRequired])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('login')
