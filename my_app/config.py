import os


class Config(object):
    SECRET_KEY = os.environ['FLASK_KEY']
