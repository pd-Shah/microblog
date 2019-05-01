from flask import (
    render_template,
    Blueprint,
    redirect,
    url_for,
    flash,
)
from app.packages.auth.forms.login import LoginForm

bp = Blueprint(
    name="auth",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/auth",
)


@bp.route("/login", methods=("POST", "GET", ))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Welcome {}, the remember status is {}".format(
                form.username.data,
                form.remember_me.data,
            )
        )
        return redirect(url_for("blog.show"))

    return render_template(
        "auth/login.html",
        form=form,
    )
