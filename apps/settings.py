# from secret_keys import CSRF_SECRET_KEY, SESSION_KEY
from datetime import timedelta

class Config(object):	
    # Set secret keys for CSRF protection
    SECRET_KEY = "rlawogus"
    # CSRF_SESSION_KEY = SESSION_KEY
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)


class Production(Config):
    DEBUG = True
    CSRF_ENABLED = False
    ADMIN = 'khuproject1515@gmail.com'
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///khu?instance=halogen-goods-865:work'
    migration_directory = 'migrations'
