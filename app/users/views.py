from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, login_user, logout_user
from app.users.forms import Signupform, Loginform

#import module models
from app import shoppers
from ..models import User
from . import users


@users.route('/')
def homepage():
    """import and render home page"""
    return render_template('home.html', title="home")
@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signupform()
    if request.method == 'POST':
        #validate signin form
        if form.validate_on_submit() == False:
            flash('Invalid email or password please try again')
            print form.errors
        else:	
            fname = form.first_name.data
            lname = form.last_name.data
            mail = form.email.data
            pswd = form.password.data
			#insert data from form to tables 
            new_user = User(fname, lname, mail, pswd)  
            shoppers.session.add(new_user)
            #commit changes
            shoppers.session.commit()
            flash('Successfully signedup')
            return redirect(url_for('users.login')) 
         
    return render_template('signup.html', form=form, title='Signup')   
 
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None:
                if user.verify_password(form.password.data):
                    login_user(user) 
                    flash('Welcome!!')
                    return redirect(url_for('lists_mod.list_items'))
                flash('Wrong password')  
            flash('Invalid email') 
    return render_template('login.html', form=form, title='login')  
 
def show_user():
    user = User.query.get_or_404(id)
    return render_template('dashboard/dashboard.html', user=user)   

 
@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    # redirect to the login page
    return redirect(url_for('users.login'))
