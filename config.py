DEBUG=True

#sdefine directory for application
import os
BASEDIR=os.path.abspath(os.path.dirname(__file__))

#define database we are working with
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASEDIR,'shoppers.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2

#set cross site request forgery
WTF_CSRF_ENABLED=True

#set a secret key for csrf
SECRET_KEY='XMAS1945mars'
