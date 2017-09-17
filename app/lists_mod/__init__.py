from flask import Flask,Blueprint

lists_mod=Blueprint('lists_mod',__name__,template_folder='templates')

from . import views