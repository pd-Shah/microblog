from flask import (
    current_app,
    g,
    request,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel
from flask_rq2 import RQ


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
mail = Mail()
babel = Babel()
rq = RQ()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])
