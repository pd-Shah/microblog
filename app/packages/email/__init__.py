from flask import Blueprint
from flask_mail import Message
from app.init import mail


bp = Blueprint(
    name="email",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/mail",
)
