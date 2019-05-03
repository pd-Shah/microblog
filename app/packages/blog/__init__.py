from flask import (
    Blueprint,
    render_template,
)
from flask_login import (
    current_user,
    login_required,
)
from app.packages.blog.models import Post


bp = Blueprint(
    name="blog",
    import_name=__name__,
    url_prefix="/blog",
    template_folder="templates"
)


@bp.route("/index", methods=["GET"], )
@login_required
def index():
    user = current_user
    posts = Post.query.all()
    return render_template("blog/index.html", user=user, posts=posts)
