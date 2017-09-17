import os
import unittest
from app import shoppers

TEST_DB='test_db.db'

class BasicTest(unittest.TestCase):
 def setUp(self):
  #setup executed for each testcase
  app.config['TESTING']=True
  app.config['WTF_CSRF_ENABLE']=False
  app.config['DEBUG']=False
  app.config['SQLALCHEMY_DATABASE-URI']='sqlite:///'+\
  os.path.join(os.app.config[basedir],'TEST_DB')
  self.app=app.test_client()
  shoppers.drop_all()
  shoppers.create_all()
  #executed after each test
 def tearDown(self):
  pass

if __name__=='__main__':
 unittest.main()
