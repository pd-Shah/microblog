from app.init import db
from app import create_app
from app.packages.auth.models import User
from app.packages.blog.models import Post

app = create_app()
with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()
    user = User(username="pd", email="pd@gmail.com", about_me="I am a big programmer. blah blah...")
    user.set_password("pd")
    db.session.add(user)
    db.session.commit()
    post = Post(header="programming", body="Flask is the best", user_id = user.id)
    db.session.add(post)
    db.session.commit()
    user = User(username="guest", email="guest@gmail.com", about_me="I am a big programmer. blah blah...")
    user.set_password("guest")
    db.session.add(user)
    db.session.commit()
    post = Post(header="programming", body="Django is the best", user_id = user.id)
    db.session.add(post)
    db.session.commit()
