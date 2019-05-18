from flask_wtf import FlaskForm
from wtforms import (
    PasswordField,
    SubmitField,
    StringField,
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
)

class ResetPasswordForm(FlaskForm):
    email = StringField(
                label="email",
                validators=[DataRequired(), Email()],
            )
    submit = SubmitField(label="send mail")
