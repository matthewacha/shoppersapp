from flask import Flask,Blueprint

users=Blueprint('users',__name__,template_folder='templates')

from . import views