from os import makedirs
from flask import (
    Flask,
    render_template,
)
from config import Config


def create_app():
    app = Flask(import_name=__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile(filename="config.py", silent=False)

    try:
        makedirs(app.instance_path, )
    except Exception as e:
        print(e)

    @app.route("/", methods=["GET", ])
    def index():
        user = {'username': 'pd'}
        posts = [
            {
                'author': {'username': 'pd'},
                'body': 'Hey there!'
            },
            {
                'author': {'username': 'SOW'},
                'body': 'HELLO!'
            },
        ]
        return render_template("index.html", user=user, posts=posts)

    return app
