from flask import (
    render_template,
    Blueprint,
    redirect,
    url_for,
    flash,
    request,
)
from flask_login import (
    current_user,
    login_user,
    logout_user,
)
from app.packages.auth.forms import (
    LoginForm,
    RegisterationForm,
)
from app.packages.auth.logics import (
    load_user,
    add_user,
)
from app.packages.utiles import is_safe
from app.packages.auth.models import User

bp = Blueprint(
    name="auth",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/auth",
)


@bp.route("/login", methods=("POST", "GET", ))
def login():
    if current_user.is_authenticated:
        return redirect(url_for("blog.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            username = form.username.data
            ).first()
        if user is None or not user.check_password(form.password.data):
            flash("username and password mixing is invalid.")
            return redirect(url_for("auth.login"))
        else:
            nxt = request.args.get("next")
            if is_safe(nxt):
                login_user(user=user, remember=form.remember_me.data)
                flash(
                    "Welcome {}.".format(user.username)
                )
                return redirect(nxt)
            else:
                flash("smell malicious user.")
                return redirect(url_for("auth.login"))
    return render_template(
        "auth/login.html",
        form=form,
    )

@bp.route("/logout", methods=["GET", ])
def logout():
    logout_user()
    flash("logout successfull.")
    return redirect(url_for("blog.index"), )

@bp.route("/register", methods=("POST", "GET",))
def register():
    if current_user.is_authenticated:
        return redirect(url_for("blog.index"))
    form = RegisterationForm()
    if form.validate_on_submit():
        add_user(form)
        return redirect(url_for("auth.login"))
    return render_template(
                "auth/register.html",
                form=form,
            )
