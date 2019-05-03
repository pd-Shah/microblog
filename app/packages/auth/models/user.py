from datetime import datetime
from hashlib import md5
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
    username = db.Column(db.String(128), unique=True,)
    password = db.Column(db.String(512), )
    email = db.Column(db.String(128), unique=True, )
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(256))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password, )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        email_hash = md5(self.email.lower().encode("utf-8")).hexdigest()
        url = "https://www.gravatar.com/avatar/{}?d=robohash&s={}".format(
                email_hash, size)
        return url

    def __repr__(self, ):
        return "<User: {}>".format(self.username)
