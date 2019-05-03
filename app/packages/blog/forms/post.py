from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
)


class PostForm(FlaskForm):
    header = StringField(
        label="header",
        validators=[DataRequired(), ],
    )
    body = TextAreaField(
        label="body",
        validators=[DataRequired(), ],
    )
    submit = SubmitField(label="submit")
