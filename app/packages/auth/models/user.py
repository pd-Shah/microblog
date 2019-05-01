from app.init import db
from app.packages.blog.models import Post


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(128), unique=True, nullable=False, )
    password = db.Column(db.String(512), nullable=False, )
    email = db.Column(db.String(128), unique=True, nullable=False, )
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __repr__(self, ):
        return "<User: {}>".format(self.username)
