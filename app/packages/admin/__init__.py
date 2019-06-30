from flask_admin.contrib.sqla import ModelView
from .models import MyModelView
from app.init import (
    db,
    admin,
)

from app.packages.auth.models import User
from app.packages.blog.models import Post
post_view = MyModelView(Post, db.session)
user_view = MyModelView(User, db.session)
admin.add_view(post_view)
admin.add_view(user_view)
