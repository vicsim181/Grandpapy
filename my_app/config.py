import os


class Config(object):
    SECRET_KEY = os.environ.get('FLASK_KEY')
