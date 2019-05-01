from datetime import datetime
from app.init import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(256), nullable=False, )
    body = db.Column(db.String(512), )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self, ):
        return "<Post: {}>".format(self.header)
