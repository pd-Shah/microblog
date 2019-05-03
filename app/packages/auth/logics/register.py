from flask import flash
from app.init import db
from app.packages.auth.models import User


def add_user(form, ):
    username = form.username.data
    password = form.password.data
    email = form.email.data
    about_me = form.about_me.data
    user = User(
            username=username,
            email=email,
            about_me=about_me,
           )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    flash("user added successfully.")
    return True
