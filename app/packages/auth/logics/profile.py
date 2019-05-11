from flask import (
    flash,
    current_app,
)
from flask_login import current_user
from app.packages.auth.models import User
from app.init import (
    db,
)

def update(form, ):
    username = form.username.data
    about_me = form.about_me.data
    user = User.query.filter_by(username=username).first()
    current_user.username = username
    current_user.about_me = about_me
    db.session.commit()
    flash("profile updated successfully.")
    return True

def followed_posts(page, ):
    posts = current_user.get_followed_posts().paginate(
                            page,
                            current_app.config["POSTS_PER_PAGE"],
                            True,
                        )
    return posts
