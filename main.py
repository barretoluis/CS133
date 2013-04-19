import jinja2
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from webapp2_extras import sessions


jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])
def mentee_key(mentee_name='default_mentee'):
	return ndb.Key('Mentee', mentee_name)

providers = {
	'Google'   : 'https://www.google.com/accounts/o8/id',
	'Yahoo'    : 'yahoo.com',
	'MySpace'  : 'myspace.com',
	'AOL'      : 'aol.com',
	'MyOpenID' : 'myopenid.com'
	# add more here
}

class Message(ndb.Model):
	author = ndb.UserProperty()
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)
class Mentee(ndb.Model):
	userid = ndb.StringProperty()
	nickname = ndb.UserProperty()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.out.write('Hello <em>%s</em>! [<a href="%s">sign out</a>]' % (user.nickname(), users.create_logout_url(self.request.uri)))
			"""else:
            self.response.out.write('Hello world! Sign in at: ')
            for name, uri in providers.items():
			    self.response.out.write('[<a href="%s">%s</a>]' % (users.create_login_url(federated_identity=uri), name))"""
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render());
	def post(self):
		if user.get_current_user():
			template = jinja_environment.get_template('services.html')
class Services(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('services.html')
		self.response.out.write(template.render());
class MenteeReg(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('menteeReg.html')
		self.response.out.write(template.render());
class AboutUs(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('aboutus.html')
		self.response.out.write(template.render())
class MyAccount(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		#shruti = Mentee(parent = mentee_key())
		shruti = Mentee()
		template = jinja_environment.get_template('myaccount.html')
		if user:
			shruti.populate(userid='123', nickname = user)
			shruti_key = shruti.put()
			#mentees_query = Mentee.query(ancestor = mentee_key())
			#mentees = mentees_query.fetch(10)
			mentees = shruti_key.get()
			self.response.out.write('shruti_key: %s Mentees: %s' % (shruti_key, mentees))
			self.response.out.write(template.render(mentees=mentees))	
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			self.response.out.write(template.render(url=url, url_linktext=url_linktext))
			#self.response.out.write('[<a href="%s">%s</a>]' % (url, url_linktext))
		##self.response.out.write(template.render());
app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/services', Services), ('/menteeReg', MenteeReg ), ('/aboutus', AboutUs ), ('/myaccount', MyAccount )
], debug=True)