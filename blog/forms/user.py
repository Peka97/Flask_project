from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    username = StringField('Username')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    confirm_password = PasswordField('Confirm Password')


class UserRegisterForm(UserBaseForm):
    password = PasswordField(
        'Password',
        [validators.DataRequired(), validators.EqualTo('confirm_password')]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        [validators.DataRequired(),]
    )
    email = StringField(
        'Email', [validators.DataRequired(), validators.Email()])
    submit = SubmitField('Register')


class UserLoginForm(UserBaseForm):
    username = StringField(
        "Username",
        [validators.DataRequired(), ],
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired(), ]
    )
    submit = SubmitField('Login')
