from flask_wtf import FlaskForm
from flask import flash
from flask_login import current_user
from app.packages.auth.logics import get_user
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    Length,
    DataRequired,
    ValidationError,
)


class EditProfileForm(FlaskForm):
    username = StringField(
                    label="username",
                    validators=[DataRequired(), ],
                )
    about_me = TextAreaField(
                label="about_me",
                validators=[
                    Length(min=0, max=256),
                    DataRequired(),
                    ]
                )
    submit = SubmitField(label="update")

    def __init__(self, username_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username_page = username_page

    def validate_username(self, username):
        if self.username_page == current_user.username:
            user = get_user(username.data)
            if user is not None:
                raise ValidationError("username is not validate.")
