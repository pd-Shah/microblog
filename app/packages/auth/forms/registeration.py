from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
    ValidationError,
)
from app.packages.auth.models import User


class RegisterationForm(FlaskForm):
    username = StringField(
                    label="username",
                    validators=(DataRequired(), ),
                )
    password = PasswordField(
                    label="password",
                    validators=(DataRequired(), ),
                )
    password_confirmation = PasswordField(
                                label="password",
                                validators=(
                                    DataRequired(),
                                    EqualTo("password")
                                ),
                            )
    email = StringField(
                label="email",
                validators=(DataRequired(), Email()),
            )
    about_me = TextAreaField(label="about me")
    submit = SubmitField("Register")

    def validate_email(self, username, ):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Choose another email address.")

    def validate_username(self, email, ):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError("Choose anther username.")
