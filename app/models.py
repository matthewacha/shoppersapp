from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from app import shoppers, login_manager


class User(shoppers.Model, UserMixin):
    __tablename__ = 'user'
    id = shoppers.Column(shoppers.Integer, primary_key=True)
    first_name = shoppers.Column(shoppers.String(60))
    last_name = shoppers.Column(shoppers.String(60))
    email = shoppers.Column(shoppers.String(60), unique=True)
    password_hash = shoppers.Column(shoppers.String(300))
    item_id = shoppers.Column(shoppers.Integer, shoppers.ForeignKey('listsitems.id'))
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    @property
    def password(self):
        """this is private stuff"""
        raise AttributeError('password is not a readable attribute.')  
   
    @password.setter  
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password) 
		
    def verify_password(self, password):
        """Check if hashed password matches actual password"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '{}'.format(self.name)
  
    #setup user loader  
    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))
 
class ListsItems(shoppers.Model):
    __tablename__ = 'listsitems'
    id = shoppers.Column(shoppers.Integer, primary_key=True)
    name = shoppers.Column(shoppers.String(60), nullable=False)
    description = shoppers.Column(shoppers.String(200), nullable=False)
    #user_id=shoppers.Column(shoppers.Integer,ForeignKey('user.id'))
    user = shoppers.relationship('User', backref='listsitems',
                                 lazy='dynamic')
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return '{} {}'.format(self.name, self.description)

    #create engine to store data in local database directory   

shoppers.Model.metadata.bind = create_engine('sqlite:///shoppers.db') 

