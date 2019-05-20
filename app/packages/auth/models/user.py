from datetime import datetime
from time import time
from jwt import (
    decode,
    encode,
)
from hashlib import md5
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)
from flask import current_app
from flask_login import (
    UserMixin,
)
from app.init import (
    db,
)
from app.packages.blog.models import Post


followers = db.Table(
    "followers",
    db.Column(
        "follower",
        db.Integer,
        db.ForeignKey("user.id"),
        primary_key=True,
    ),
    db.Column(
        "followed",
        db.Integer,
        db.ForeignKey("user.id"),
        primary_key=True,
    ),
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(128), unique=True,)
    password = db.Column(db.String(512), )
    email = db.Column(db.String(128), unique=True, )
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(256))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
                    "User",
                    secondary=followers,
                    primaryjoin=id==followers.c.follower,
                    secondaryjoin=id==followers.c.followed,
                    backref=db.backref("followers", lazy="dynamic"),
                    lazy="dynamic",
                )

    def set_password(self, password):
        self.password = generate_password_hash(password, )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        email_hash = md5(self.email.lower().encode("utf-8")).hexdigest()
        url = "https://www.gravatar.com/avatar/{}?d=robohash&s={}".format(
                    email_hash, size)
        return url

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        if self.followed.filter_by(id=user.id).first():
            return True
        return False

    def is_followed(self, user):
        if self.followers.filter_by(id=user.id).first():
            return True
        return False

    def get_followed_posts(self, ):
        query = Post.query.join(
                    followers,
                    (followers.c.followed==Post.user_id)
                ).filter(followers.c.follower==self.id).order_by(
                                                        Post.timestamp.desc()
                                                        )
        return query

    @staticmethod
    def get_user_by_username(username, ):
        user = User.query.filter_by(
            username = username
            ).first()
        return user

    @staticmethod
    def get_user_by_email(user_email, ):
        user = User.query.filter_by(
            email=user_email
        ).first()
        return user

    def set_lastseen(self, ):
        self.last_seen = datetime.utcnow()

    def build_jwt_token(self, exp=600, ):
        payload = {
                    "exp": time() + exp,
                    "id": self.id,
                }
        key = current_app.config["SECRET_KEY"]
        token = encode(payload=payload, key=key, algorithm='HS256')
        token = token.decode("utf-8")
        return token

    @staticmethod
    def get_user_by_token(token, ):
        try:
            key = current_app.config["SECRET_KEY"]
            obj = decode(jwt=token, key=key, algorithms=["HS256", ])
            id = obj.get("id")
            return User.query.get(id)
        except Exception as e:
            return None

    def __repr__(self, ):
        return '<%s.%s: %s, object at %s>' % (
            self.__class__.__module__,
            self.__class__.__name__,
            self.username,
            hex(id(self))
        )
