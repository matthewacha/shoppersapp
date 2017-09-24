from flask import Flask
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app =Flask(__name__)

#### config ####

 
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
 
shoppers = SQLAlchemy(app)
shoppers.create_all()

#####login requirements
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "users.login"
 
migrate = Migrate(app, shoppers)

from app import models

#import module component as its blueprint
from .users import users as users_blueprint
from .lists_mod import lists_mod as lists_blueprint

#register blueprints
app.register_blueprint(lists_blueprint)
app.register_blueprint(users_blueprint)

