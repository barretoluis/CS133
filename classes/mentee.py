'''
Created on Apr 19, 2013

@author: luis
'''
from google.appengine.ext import ndb

class mentee(ndb.Model):
    '''
    Mentee database entity class. Defines the table mentee
    '''
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty()
    birthDate = ndb.StringProperty()
    foi = ndb.StringProperty()
    degree = ndb.StringProperty()
    yog = ndb.StringProperty()
    backDes = ndb.StringProperty()
    gender = ndb.StringProperty()
    zipCode = ndb.StringProperty()
    ethnicity = ndb.StringProperty()