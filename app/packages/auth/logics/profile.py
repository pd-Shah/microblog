from flask import flash
from flask_login import current_user
from app.init import db
from app.packages.auth.models import User

def update(form, ):
    username = form.username.data
    about_me = form.about_me.data
    user = User.query.filter_by(username=username).first()
    if current_user.id == user.id:
        current_user.username = username
        current_user.about_me = about_me
        db.session.commit()
        flash("profile updated successfully.")
    return True
