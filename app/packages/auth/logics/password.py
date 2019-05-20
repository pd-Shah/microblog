from flask import flash
from app.init import db
from app.packages.auth.models import User

def change_password(token, new_password, ):
    user = User.get_user_by_token(token)
    if user is None:
        flash("token is not valid")
        return None
    user.set_password(new_password)
    db.session.commit()
    return user
