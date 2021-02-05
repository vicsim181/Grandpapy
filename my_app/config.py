import os


class Config(object):
    SECRET_KEY = os.environ.get('flask_key')
