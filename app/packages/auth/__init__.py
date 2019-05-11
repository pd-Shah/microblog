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
    login_required,
)
from app.packages.auth.forms import (
    LoginForm,
    RegisterationForm,
    EditProfileForm
)
from app.packages.auth.logics import (
    load_user,
    add_user,
    get_user,
    set_lastseen,
    update,
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
        user = get_user(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash("username and password mixing is invalid.")
            return redirect(url_for("auth.login"))
        nxt = request.args.get("next")
        if is_safe(nxt):
            login_user(user=user, remember=form.remember_me.data)
            set_lastseen()
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
        return redirect(url_for("blog.index"))
    return render_template(
                "auth/register.html",
                form=form,
            )

@bp.route("/profile/<string:username>")
@login_required
def profile(username, ):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts
    return render_template("auth/profile.html",
                            user=user,
                            posts=posts,
            )

@bp.route("/profile/<string:username>/edit", methods=["POST", "GET", ])
@login_required
def update_profile(username, ):
    form = EditProfileForm(username, )
    if form.validate_on_submit():
        update(form, )
        return redirect(
                url_for(
                    "auth.profile",
                    username=current_user.username,
                    )
                )

    user = User.query.filter_by(username=username).first_or_404()
    form.username.data = user.username
    form.about_me.data = user.about_me
    return render_template("auth/edit_profile.html", form=form, user=user)

@bp.route("/follow/<string:username>")
@login_required
def follow(username, ):
    user = get_user(username)
    current_user.follow(user)
    return redirect(url_for('auth.profile', username=username))


@bp.route("/unfollow/<string:username>")
@login_required
def unfollow(username, ):
    user = get_user(username)
    current_user.unfollow(user)
    return redirect(url_for("auth.profile", username=username))
