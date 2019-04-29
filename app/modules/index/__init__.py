from flask import (
    Blueprint,
    render_template,
)


bp = Blueprint(
    name="index",
    import_name=__name__,
    url_prefix="/index",
    template_folder="templates"
)


@bp.route("/", methods=["GET"], )
def show():
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
    return render_template("index/index.html", user=user, posts=posts)
