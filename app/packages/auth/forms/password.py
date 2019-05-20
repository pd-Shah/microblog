from flask_wtf import FlaskForm
from wtforms import (
    PasswordField,
    SubmitField,
    StringField,
)
from wtforms.validators import (
    DataRequired,
    Email,
)

class ForgetPasswordForm(FlaskForm):
    email = StringField(
                label="email",
                validators=[DataRequired(), Email()],
            )
    submit = SubmitField(label="send mail")


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
                    label="password",
                    validators=[DataRequired(),],
                )
    submit = SubmitField(label="Reset My Password")
