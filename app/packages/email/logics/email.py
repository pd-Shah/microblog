from flask_mail import Message
from app.init import mail
from flask import (
    render_template,
    current_app,
)
from app.packages.auth.models import User


def _send_mail(sender, recipients, subject, header, body):
    msg = Message(
            subject=subject,
            recipients=recipients,
            sender=sender,
        )
    msg.header = header
    msg.html = body
    mail.send(msg)

def send_forget_password(user_email, ):
    sender = current_app.config["ADMIN"]
    recipients = [user_email, ]
    subject = "Forget Password"
    header = "Change Password Request"
    user = User.get_user_by_email(user_email)
    body = render_template(
                "email/forget_password.html",
                 user=user,
            )
    _send_mail(sender, recipients, subject, header, body)
