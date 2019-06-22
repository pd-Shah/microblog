from marshmallow import Schema
from marshmallow.fields import (
    String,
    DateTime,
)


class PostSchema(Schema):
    header = String()
    body = String()
    timestamp = DateTime()
