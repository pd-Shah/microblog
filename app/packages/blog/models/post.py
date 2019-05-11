from datetime import datetime
from app.init import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(256), )
    body = db.Column(db.String(512), )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def add_post(user_id, header, body):
        post = Post(header=header, body=body)
        post.user_id = user_id
        return post

    @staticmethod
    def get_post_by_id(id, ):
        post = Post.query.get(id)
        return post

    def edit_post(self, header, body):
        self.header = header
        self.body = body

    def __repr__(self, ):
        return "<Post: {}>".format(self.header)
