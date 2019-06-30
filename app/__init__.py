from os import makedirs
from redis import Redis
import rq_dashboard
from flask import (
    Flask,
    render_template,
    request,
)
from settings import Config
from app.init import (
    db,
    migrate,
    login,
    mail,
    babel,
    rq,
    admin,
)
from app.packages import admin as _
from app.packages import blog
from app.packages import auth
from app.packages import error
from app.packages import email
from app.packages import api
from app.packages import payment
from app.packages import sms


def create_app():
    app = Flask(import_name=__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile(filename="config.py", silent=False)
    app.config.from_object(rq_dashboard.default_settings)
    db.init_app(app, )
    migrate.init_app(app, db, )
    login.init_app(app, )
    mail.init_app(app, )
    babel.init_app(app, )
    rq.init_app(app, )
    admin.init_app(app, )
    try:
        makedirs(app.instance_path, exist_ok=True)
    except Exception as e:
        print(e)
    app.register_blueprint(blog.bp, )
    app.register_blueprint(auth.bp, )
    app.register_blueprint(error.bp, )
    app.register_blueprint(email.bp, )
    app.register_blueprint(api.bp, )
    app.register_blueprint(payment.bp, )
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq", )
    app.register_blueprint(sms.bp, )

    return app
