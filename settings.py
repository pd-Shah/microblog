from os import environ


class Config():
    SECRET_KEY = environ.get(key="SECRET_KEY", default="development")
    POSTS_PER_PAGE = 2
