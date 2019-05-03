from datetime import datetime
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
    user = User.query.filter_by(
        username = username
        ).first()
    return user

def set_lastseen():
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
    return True
