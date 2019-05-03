from app.packages.auth.models import User
from app.init import login


@login.user_loader
def load_user(user_id, ):
    return User.query.get(user_id)
