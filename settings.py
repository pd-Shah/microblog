from os import environ


class Config():
    SECRET_KEY = environ.get(key="SECRET_KEY", default="development")
    POSTS_PER_PAGE = 10
    ADMIN = environ.get("ADMIN")
    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = environ.get("MAIL_USE_TLS")
    MAIL_PORT =  environ.get("MAIL_PORT")
    LANGUAGES = ['de', 'fa', 'en']
