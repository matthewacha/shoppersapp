import sqlite3
from flask import render_template,request,url_for,redirect,flash,g,session
from flask_login import login_required,login_user,logout_user
from werkzeug import generate_password_hash
from app.users import forms
from forms import Signupform,Loginform
#import module models
from app import models
from ..models import User
from . import users
from app import shoppers

@users.route('/')
def homepage():
 """import and render home page"""
 return render_template('home.html',title="home")
 
@users.route('/signup',methods=['GET','POST'])
def signup(): 
 form=Signupform()
 if request.method=='POST':
 
#validate signin form 
  if form.validate():
   fname=form.first_name.data
   lname=form.last_name.data
   mail=form.email.data
   pswd=form.password.data
  
  #insert data from form to tables  
   new_user=User(fname,lname,mail,pswd)  
   shoppers.session.add(new_user)
  
  #commit changes
   shoppers.session.commit()
   flash('Successfully signedup,Please login to verify account')
   return redirect(url_for('users.login')) 
  flash('Invalid email or password please try again') 
 return render_template('signup.html',form=form,tile='Signup')   
 
@users.route('/dashboard')
@login_required
def dashboard():
 return render_template('dashboard.html',title='Dashboard') 
 
@users.route('/login',methods=['GET','POST'])
def login():
 form=Loginform()
 if request.method=='POST':
  if form.validate_on_submit():
   user=User.query.filter_by(email=form.email.data).first()
   if user is not None:
    if user.verify_password(form.password.data):
     login_user(user)
     return redirect(url_for('users.dashboard'))
    flash('Wrong password')  
   flash('Invalid email')  
 return render_template('login.html',form=form,title='login')
 
@users.route('/logout')
@login_required
def logout():
 logout_user()
 flash('You have successfully been logged out.')
# redirect to the login page
 return redirect(url_for('users.login'))