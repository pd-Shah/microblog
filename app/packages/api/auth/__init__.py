from flask import (
    g,
    jsonify,
)
from flask_httpauth import (
    HTTPBasicAuth,
    HTTPTokenAuth,
    MultiAuth,
)
from flask_restful import Resource
from app.packages.auth.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')
auth = MultiAuth(token_auth, basic_auth)


class TokenApi(Resource):

    @auth.login_required
    def get(self, ):
        user = g.current_user
        token = user.build_token().decode("ascii")
        return jsonify({"token": token, })


@basic_auth.verify_password
def verify_pw(username, password):
    user = User.get_user_by_username(username)
    if user is not None:
        if user.check_password(password):
            g.current_user = user
            return True
    else:
        return False


@token_auth.verify_token
def verify_tk(token):
    user = User.verify_user_token(token)
    if user is not None:
        g.current_user = user
        return True
    else:
        return False
