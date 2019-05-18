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
    EditProfileForm,
    ResetPasswordForm,
)
from app.packages.auth.logics import (
    load_user,
    add_user,
    get_user,
    set_lastseen,
    update,
    do_follow,
    do_unfollow,
    followed_posts,
)
from app.packages.email.logics import send_forget_password
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
    page = request.args.get("page", 1, type=int)
    f_posts = followed_posts(page)
    return render_template("auth/profile.html",
                            user=user,
                            posts=posts,
                            paginate=f_posts,
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
    do_follow(username)
    return redirect(url_for('auth.profile', username=username))


@bp.route("/unfollow/<string:username>")
@login_required
def unfollow(username, ):
    do_unfollow(username)
    return redirect(url_for("auth.profile", username=username))


@bp.route("/forget", methods=["POST", "GET"])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for("blog.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if not User.get_user_by_email(form.email.data):
            flash("unregistred email address.")
            return redirect(url_for("auth.reset_password"))
        send_forget_password(form.email.data)
        flash("check your email to continue")
        return redirect(url_for("blog.index"))
    return render_template(
                "auth/forget_password.html",
                form=form,
            )
