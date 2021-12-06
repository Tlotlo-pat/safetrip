import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'modzy modelops are incredible'

    API_URL = os.environ.get('API_URL') or "https://app.modzy.com/api"
    API_KEY = os.environ.get(
        'API_KEY') or "bjBDzSU8ZWr3yOFSYVXn.SL2IF0m0PBaY7aCR1Nvw"

    DEBUG = os.environ.get('FLASK_DEBUG') or 0
