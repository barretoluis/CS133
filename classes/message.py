'''
Created on Apr 19, 2013

@author: luis
'''
from google.appengine.ext import ndb
class message(object):
    '''
    classdocs
    '''
    fromUser = ndb.StringProperty()
    toUser = ndb.StringProperty()
    message = ndb.StringProperty()
