from flask import (
     Blueprint,
     current_app,
     render_template,
)
from flask_mail import Message
from app.init import mail
from app.packages.auth.models import User
from app.packages.email.logics import send_mail


bp = Blueprint(
    name="email",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/mail",
)


def send_forget_password(user_email, ):
    sender = current_app.config["ADMIN"]
    recipients = [user_email, ]
    subject = "Forget Password"
    header = "Change Password Request"
    user = User.get_user_by_email(user_email)
    token = user.build_jwt_token()
    body = render_template(
                "email/forget_password.html",
                 user=user,
                 token=token,
            )
    send_mail.queue(sender, recipients, subject, header, body)
