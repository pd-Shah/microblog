from os import environ
from os.path import (
    abspath,
    dirname,
    join,
)


base_directory = abspath(dirname(__file__))
SQLALCHEMY_DATABASE_URI = environ.get(
    key="DATABASE_URL",
    default="sqlite:///{0}".format(join(base_directory, "db")),
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
