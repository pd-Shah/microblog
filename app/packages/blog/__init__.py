from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
)
from app.packages.blog.forms import (
    PostForm,
)
from app.packages.blog.logics import (
    add_post,
    get_post,
    update_post,
    delete_post,
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


@bp.route("/add", methods=["GET", "POST"], )
@login_required
def add():
    form = PostForm()
    if form.validate_on_submit():
        add_post(form)
        return redirect(url_for("blog.index"))
    return render_template("blog/add_post.html", form=form, )


@bp.route("/edit/<int:id>", methods=["POST", "GET", ])
@login_required
def edit(id, ):
    form = PostForm()
    if form.validate_on_submit():
        update_post(id, form)
        return redirect(url_for("blog.index"))
    post = get_post(id, )
    form.header.data = post.header
    form.body.data = post.body
    return render_template("blog/add_post.html", form=form)


@bp.route("/delete/<int:id>", methods=["GET", "POST"], )
@login_required
def delete(id, ):
    delete_post(id)
    return redirect(url_for("blog.index"))
