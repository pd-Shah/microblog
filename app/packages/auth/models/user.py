from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)
from flask_login import UserMixin
from app.init import (
    db,
)
from app.packages.blog.models import Post


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(128), unique=True, nullable=False, )
    password = db.Column(db.String(512), nullable=False, )
    email = db.Column(db.String(128), unique=True, nullable=False, )
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password = generate_password_hash(password, )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self, ):
        return "<User: {}>".format(self.username)
