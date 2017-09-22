#-*- coding:utf-8 -*-
import os
import unittest
from flask import url_for
from app import app, shoppers


TEST_DB = 'test_db'
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class BasicTest(unittest.TestCase):
    def setUp(self):
  #setup executed for each testcase
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLE'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+\
        os.path.join(BASEDIR, 'TEST_DB')
        self.app = app.test_client()
        shoppers.drop_all()
        shoppers.create_all()
  #executed after each test
    def tearDown(self):
        pass 
  ##helper methods
    def signup(self, first_name, last_name, email, password):
        return self.app.post('/signup', data=dict(fname=first_name,\
		lname=last_name, mail=email, pswd=password), follow_redirects=True)  
    def login(self, email, password):
        return self.app.post(url_for('users.login'), data=dict(email=email, \
		password=password), follow_redirects=True) 
  ##tests
    def test_indexpage(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_signup_form_displays(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'First name', response.data) 
		
    def test_valid_signup(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.signup('Max', 'Antony', 'max@gmail.com', 'ambassador')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully signedup', response.data) 	
		
    def test_invalid_signup(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.signup('Max', 'Antony', 'max@gmail.com', 'ambassador')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email or password please try again', response.data) 
  
    def test_login(self):
        with app.app_context():
            self.app.get('/signup',follow_redirects=True)
            self.signup('Max', 'Antony', 'max@gmail.com', 'ambassador')	
            self.app.get('/login', follow_redirects=True)			
            response = self.login('max@gmail.com', 'ambassador')
            #self.assertEqual(response.status_code, 200)
            self.assertIn(b'Remember me', response.data)###wrong stuff
  
if __name__ == '__main__':
    unittest.main()
