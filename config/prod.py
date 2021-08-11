import os
DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
QLALCHEMY_TRACK_MODIFICATIONS = False

#DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/flask'
#SQLALCHEMY_TRACK_MODIFICATIONS = False