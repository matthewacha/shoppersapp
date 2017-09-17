import os
import unittest
from flask_sqlalchemy import sqlalchemy
from app import app,shoppers


TEST_DB='test_db'
BASEDIR=os.path.abspath(os.path.dirname(__file__))

class BasicTest(unittest.TestCase):
 def setUp(self):
  #setup executed for each testcase
  app.config['TESTING']=True
  app.config['WTF_CSRF_ENABLE']=False
  app.config['DEBUG']=False
  app.config['SQLALCHEMY_DATABASE-URI']='sqlite:///'+\
  os.path.join(BASEDIR,'TEST_DB')
  self.app=app.test_client()
  shoppers.drop_all()
  shoppers.create_all()
  #executed after each test
 def tearDown(self):
  pass
  
  ##helper methods
 def signup(self,first_name,last_name,email,password):
  return self.app.post('/signup',data={first_name:first_name,last_name:last_name,\
  email:email,password:password},follow_redirects=True)
  
 def login(self,email,password):
  return self.app.post('/login',data={email:email,password:password},follow_redirects=True) 
  ##tests
 def test_indexpage(self):
  response=self.app.get('/',follow_redirects=True)
  self.assertEqual(response.status_code,200)
  
 def test_valid_signup(self):
  response=self.signup('Max','Antony','max@gmail.com','ambassador')
  self.assertEqual(response.status_code,200)
  self.assertIn('Successfully signedup',response.data) 
  
 def test_login(self):  
  response=self.login('max@gmail.com','ambassador')
  self.assertEqual(response.status_code,200)
  self.assertIn(u'',response.data)
  
if __name__=='__main__':
 unittest.main()
