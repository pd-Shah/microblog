from faker import Faker
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
    fake = Faker()
    user = User(username="pd", email=fake.email(), about_me=fake.address(), )
    user.set_password("pd")
    db.session.add(user)
    db.session.commit()

    post = Post(header=fake.name(), body=fake.text(), user_id = user.id)
    db.session.add(post)
    db.session.commit()

    user = User(username=fake.name(), email=fake.email(), about_me=fake.address(), )
    user.set_password("pass")
    db.session.add(user)
    db.session.commit()

    post = Post(header=fake.name(), body=fake.text(), user_id = user.id)
    db.session.add(post)
    db.session.commit()

    user = User(username=fake.name(), email=fake.email(), about_me=fake.address(), )
    user.set_password("pass")
    db.session.add(user)
    db.session.commit()

    post = Post(header=fake.name(), body=fake.text(), user_id = user.id)
    db.session.add(post)
    db.session.commit()

    post = Post(header=fake.name(), body=fake.text(), user_id = user.id)
    db.session.add(post)
    db.session.commit()

    pd = User.query.get(1)
    guest = User.query.get(2)
    ms = User.query.get(3)
    guest.follow(pd)
    guest.follow(ms)
    ms.follow(guest)
    pd.follow(ms)
    db.session.commit()
