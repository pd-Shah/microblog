from time import sleep
from flask_mail import Message
from app.init import (
    mail,
    rq,
)


@rq.job
def send_mail(sender, recipients, subject, header, body):
    msg = Message(
            subject=subject,
            recipients=recipients,
            sender=sender,
        )
    msg.header = header
    msg.html = body
    mail.send(msg)
