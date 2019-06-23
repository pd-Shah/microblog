from flask import (
    Blueprint,
)
from flask_restful import (
    Api,
)
from .user import (
    UserApi,
    UserListApi,
)
from .auth import (
    TokenApi,
)
bp = Blueprint(
        name="api",
        import_name=__name__,
        url_prefix="/api/v1",
    )
api = Api(bp)
api.add_resource(UserApi, "/user/<user_id>")
api.add_resource(UserListApi, "/user")
api.add_resource(TokenApi, "/token")
