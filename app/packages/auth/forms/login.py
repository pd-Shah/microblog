from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(
        label="username",
        validators=[DataRequired(message="username is required!"), ],
        description='Enter your username.',
    )
    password = PasswordField(
        label="password",
        validators=[DataRequired(message="password is required!")],
        description='Enter your password.'
    )
    submit_button = SubmitField(
        label="SingIn",
    )
    remember_me = BooleanField(
        label="remember_me"
    )
