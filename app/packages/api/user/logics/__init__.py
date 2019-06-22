from flask import abort
from app.init import db
from app.packages.auth.models import User


def get_user_by_id(user_id, ):
    user = None
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return user


def add_user(username, password, email, about_me):
    user = User(
            username=username,
            email=email,
            about_me=about_me,
           )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return True


def get_users():
    users = User.query.all()
    return users


def delete_user(user_id):
    User.delete_user_by_id(user_id)
    return user_id


def update_user(user_id, data=None):
    if data is not None:
        user = User.update_user_by_id(user_id, data)
    return user
