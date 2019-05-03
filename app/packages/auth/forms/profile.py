from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    Length,
    DataRequired,
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
