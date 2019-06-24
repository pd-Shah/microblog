from flask import (
    request,
    jsonify,
    abort
)
from flask_restful import Resource
from .schemas import (
    UserSchema,
    SafeUserSchema,
)
from .logics import (
    get_user_by_id,
    add_user,
    get_users,
    delete_user,
    update_user,
)
from app.packages.api.auth import auth


class UserApi(Resource):
    user_schema = UserSchema()
    safe_user_schema = SafeUserSchema()

    @auth.login_required
    def get(self, user_id):
        user = get_user_by_id(user_id, )
        return self.safe_user_schema.dump(user)

    @auth.login_required
    def put(self, user_id):
        info = self.user_schema.load(request.form).data
        user = update_user(user_id, info)
        return self.safe_user_schema.dump(user)

    @auth.login_required
    def delete(self, user_id):
        delete_user(user_id)
        return user_id


class UserListApi(Resource):
    user_schema = UserSchema()
    safe_user_schema = SafeUserSchema()

    @auth.login_required
    def get(self, ):
        users = get_users()
        return self.safe_user_schema.dump(users, many=True)

    @auth.login_required
    def post(self, ):
        user = self.user_schema.load(request.form).data
        add_user(**user)
        return self.user_schema.dump(user)
