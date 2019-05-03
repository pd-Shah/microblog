from flask import flash
from flask_login import current_user
from app.packages.blog.models import Post
from app.init import db


def add_post(form, ):
    header = form.header.data
    body = form.body.data
    post = Post(header=header, body=body)
    post.user_id = current_user.id
    db.session.add(post)
    db.session.commit()
    flash("post added sucessfully.")
    return True

def update_post(id, form):
    header = form.header.data
    body = form.body.data
    post = Post.query.get(id)
    if current_user.id == post.author.id:
        post.header = header
        post.body = body
        db.session.commit()
        flash("post updated successfully")
    return True

def delete_post(id, ):
    post = Post.query.get(id)
    if current_user.id == post.author.id:
        db.session.delete(post)
        db.session.commit()
        flash("post deleted successfully.")
    return True

def get_post(id, ):
    post = Post.query.get(id)
    return post
