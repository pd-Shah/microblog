from os import makedirs
from flask import (
    Flask,
    render_template,
)
from settings import Config
from app.init import (
    db,
    migrate,
)
from app.packages import blog
from app.packages import auth
from app.packages.auth.models import User


def create_app():
    app = Flask(import_name=__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile(filename="config.py", silent=False)
    db.init_app(app)
    migrate.init_app(app, db)
    try:
        makedirs(app.instance_path, )
    except Exception as e:
        print(e)
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)
    return app
