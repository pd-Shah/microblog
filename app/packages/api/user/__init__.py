from flask_restful import Resource
from .schemas import UserSchema


class UserApi(Resource):
    user_schema = UserSchema()

    def get(self, ):
        return self.user_schema.dump(dict(username="pd"))

    def post(self, ):
        return self.user_schema.dump(dict(username="pd"))

    def delete(self, ):
        return self.user_schema.dump(dict(username="pd"))
