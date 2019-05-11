from flask_login import current_user
from app.packages.auth.models import User
from app.init import (
    login,
    db,
)


@login.user_loader
def load_user(user_id, ):
    return User.query.get(user_id)

def get_user(username, ):
    user = User.get_user_by_username(username, )
    return user

def do_follow(username, ):
    user = get_user(username)
    current_user.follow(user, )
    db.session.commit()

def do_unfollow(username, ):
    user = get_user(username)
    current_user.unfollow(user, )
    db.session.commit()

def set_lastseen():
    current_user.set_lastseen()
    db.session.commit()
    return True
