from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    posts = fields.List(fields.Str())
    about_me = fields.Str()
    last_seen = fields.DateTime()
    followed = fields.List(fields.Str())
