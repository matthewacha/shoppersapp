import os
import sys
import sqlite3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from app import shoppers,login_manager
Base=declarative_base()

class User(shoppers.Model,UserMixin):
 __tablename__='user'
 id= shoppers.Column(shoppers.Integer,primary_key=True)
 first_name= shoppers.Column(shoppers.String(60))
 last_name= shoppers.Column(shoppers.String(60))
 email= shoppers.Column(shoppers.String(60),unique=True)
 password_hash= shoppers.Column(shoppers.String(300))
 def __init__(self,first_name,last_name, email, password):
   self.first_name=first_name
   self.last_name=last_name
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
  return '<User {}>'.format(self.name)
  
#setup user loader  
 @login_manager.user_loader
 def get_user(id):
  return User.query.get(int(id))
 
class Lists(shoppers.Model):
 __tablename__='lists'
 id=shoppers.Column(shoppers.Integer,primary_key=True)
 name=shoppers.Column(shoppers.String(60),nullable=False)
 #user_id=shoppers.Column(shoppers.Integer,ForeignKey('user.id'))
 #user = relationship(User)
 def __repr__(self):
  return '<Lists {}>'.format(self.name)

#create engine to store data in local database directory  
engine = create_engine('sqlite:///shoppers.db')  

shoppers.Model.metadata.bind = engine

