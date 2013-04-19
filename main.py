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
class DictModel(ndb.Model):
	def to_dict(self):
		return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Mentee(DictModel):
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	email = ndb.StringProperty()
	password = ndb.StringProperty()
	birthDate = ndb.StringProperty()
	foi = ndb.StringProperty()
	degree = ndb.StringProperty()
	yog = ndb.StringProperty()
	backDes = ndb.StringProperty()
	gender = ndb.StringProperty()
	zipCode = ndb.StringProperty()
	ethnicity = ndb.StringProperty()

class SessionHandler(webapp2.RequestHandler):
	def dispatch(self):
	# Get a session store for this request.
		self.session_store = sessions.get_store(request=self.request)
		try:
		# Dispatch the request.
			webapp2.RequestHandler.dispatch(self)
		finally:
		# Save all sessions.
			self.session_store.save_sessions(self.response)
	@webapp2.cached_property
	def session(self):
	# Returns a session using the default cookie key.
		return self.session_store.get_session()

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
class MenteeReg2(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('menteeReg2.html')
		self.response.out.write(template.render());	
	

class MenteeRegHandler(SessionHandler):
	def post(self):
		self.session['firstName'] = self.request.get('firstName')
		self.session['lastName'] = self.request.get('lastName')
		self.session['email'] = self.request.get('email')
		self.session['birthDate'] = self.request.get('birthDate')
		self.session['password'] = self.request.get('password')
		"""user = Mentee()
		user.fN = self.request.get('fN')
		user.lastName = self.request.get('lastName')
		user.email = self.request.get('email')
		user.birthDate = self.request.get('birthDate')
		user.password = self.request.get('password')
		user.put()"""
		self.redirect('/MR')
class MenteeRegHandler2(SessionHandler):
	def post(self):
		user = Mentee()
		user.firstName = self.session.get('firstName')
		user.lastName = self.session.get('lastName')
		user.email = self.session.get('email')
		user.birthDate = self.session.get('birthDate')
		user.password = self.session.get('password')
		self.session['foi'] = self.request.get('foi')
		self.session['degree'] = self.request.get('degree')
		self.session['yog'] = self.request.get('yog')
		self.session['bd'] = self.request.get('bd')
		self.session['gender'] = self.request.get('gender')
		self.session['zipCode'] =  self.request.get('zipCode')
		self.session['ethnicity'] = self.request.get('ethnicity')
		user.degree = self.session.get('degree')
		user.foi = self.session.get('foi')
		user.yog = self.session.get('yog')
		user.backDes = self.session.get('bd')
		user.gender = self.session.get('gender')
		user.zipCode = self.session.get('zipCode')
		user.ethnicity = self.session.get('ethnicity')
		user_key = user.put()
		#user = user_key.get()
		#self.session['user_key'] = user_key
		#self.refresh()
		self.redirect('/myaccount')
class MyAccount (SessionHandler):
	def get(self):
		firstName = self.session.get('firstName')
		lastName = self.session.get('lastName')
		email = self.session.get('email')
		birthDate = self.session.get('birthDate')
		password = self.session.get('password')
		degree = self.session.get('degree')
		foi = self.session.get('foi')
		yog = self.session.get('yog')
		backDes = self.session.get('bd')
		gender = self.session.get('gender')
		zipCode = self.session.get('zipCode')
		ethnicity = self.session.get('ethnicity')
		params = {
			'firstName' : firstName,
			'lastName' : lastName,
			'email' : email,
			'birthDate' : birthDate,
			'password' : password,
			'degree' : degree,
			'foi' : foi,
			'yog' : yog,
			'backDes' : backDes,
			'gender' : gender,
			'zipCode' : zipCode,
			'ethnicity' : ethnicity
		}
		#user = 
		#user = Mentee()
		#user = self.session.get('user_key')
		#user = Mentee.get_by_id('user')
		"""users_query = Mentee.query()
		users = users_query.fetch(100)
		template_values = {'users' : users}"""
		template = jinja_environment.get_template('myaccount.html')
		self.response.out.write(template.render(params))
		#user = users.get_current_user()
class AboutUs(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('aboutus.html')
		self.response.out.write(template.render())

		#shruti = Mentee(parent = mentee_key())
		"""shruti = Mentee()
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
		##self.response.out.write(template.render());"""

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'pelusa2k2',
}

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/services', Services), ('/menteeReg', MenteeReg ), ('/aboutus', AboutUs),
    	('/MRH', MenteeRegHandler), ('/MR', MenteeReg2), ('/MRH2', MenteeRegHandler2),
    	('/myaccount', MyAccount)
], debug=True, config = config)