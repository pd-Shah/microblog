from app.packages.api.post.schemas import PostSchema
from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    posts = fields.Nested(PostSchema, many=True)
    about_me = fields.Str()
    last_seen = fields.DateTime()
    followed = fields.Nested("self", many=True, exclude=("followed", ), )
