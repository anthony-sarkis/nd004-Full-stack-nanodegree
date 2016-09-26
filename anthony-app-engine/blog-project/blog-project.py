#!/usr/bin/env python
import os
import webapp2
import jinja2
import re
from string import letters
import hashlib
import hmac
import string
import random

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "html")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

# Hashing and password functions ##############

# normally would not store in this file
SECRET = 'imsosecret'
def hash_str(s):
    # call hmac passing secret phrase and phrase variable
    x = hmac.new(SECRET,s).hexdigest()
    return x

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    x = h.split('|')[0]
    if make_secure_val(x) == h:
        return x

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# Make password hash
# assign salt to default to None
def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    # Create the sha256 hash using combo of name, password, and salt
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

# Verify password by matching
def valid_pw(name, pw, h):
    # Split apart the salt from the hash
    salt = h.split(',')[1]
    # Determine if password is valid by comparing new hash to old hash
    return make_pw_hash(name, pw, salt) == h
    # return true

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

# Call data store object
class User(db.Model):
    # set parameters
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    # functions
    @classmethod
    def by_id(cls, uid):
        # get by id is built in
        # pass user ID
        return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        # return by name, basically select all by name where user =
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email = None):
        # Make password hash
        pw_hash = make_pw_hash(name, pw)
        # Return user, with pw_hash instead of pw
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u


###############################


class Handler(webapp2.RequestHandler):
    # Create a template for "write" function
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    # Create a template for rending a string
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    # cals make secure val, and sets cookie
    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        # get cookie value
        cookie_val = self.request.cookies.get(name)
        # return value if it's secure?
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    # Log user out by setting Cookie to = nothing, use path to control pages
    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    # Check if user logged in or not for user cookie, stores user object?
    # Helps keep track on every page?
    def initialize(self, *a, **kw):
            webapp2.RequestHandler.initialize(self, *a, **kw)
            uid = self.read_secure_cookie('user_id')
            self.user = uid and User.by_id(int(uid))

# Cookies

class Cookies(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        # starting point for cookie string function
        visits_cookie_str = self.request.cookies.get('visits')
        # validate cookie str
        if visits_cookie_str:
            # pass visits cookie string to check secure value function
            # secure value function is implemented above
            cookie_val = check_secure_val(visits_cookie_str)
            if cookie_val:
                visits = int(cookie_val)

        # increment visits by 1, this is valid as visits are reset to 0 if hash invalid
        visits += 1

        # pass visits to make secure value to return as string?
        new_cookie_val = make_secure_val(str(visits))

        # set cookie based on visits
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        # inform user how many times they have been to the site based on the cookie
        self.write("You've been here %s times!" % visits)

# End Cookies section



# Blog section   ###############
# TODO Comment this code.

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)

# render all posts blog front page
class BlogFront(Handler):
    def get(self):
        # Get posts from DB. Select all from Post table order by created
        posts = db.GqlQuery("select * from Post order by created desc limit 10")
        # Render front page, pass "posts" variable as posts
        self.render('front.html', posts = posts)

# Render a specific post
class PostPage(Handler):
    def get(self, post_id):
        # Create key. Find post from post_id
        # Call int to transform string from URL into integer post ID
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # Look up a specific item in the db using key
        post = db.get(key)

        # Return error if no valid key
        if not post:
            self.error(404)
            return

        # Render page using Permalink HTML as a template, pass post var as post
        self.render("permalink.html", post = post)

# Handle new post
class NewPost(Handler):
    """ TODO describe me """
    
    # Render new post HTML
    def get(self):
        self.render("newpost.html")

    # On Post render
    def post(self):
        # Get variables passed from form
        subject = self.request.get('subject')
        content = self.request.get('content')

        # Handle if valid post
        if subject and content:
            # Create new post as p variable
            p = Post(parent = blog_key(), subject=subject, content=content)
            # Store element (p) in database
            p.put()
            # Redirect to blog page using ID of element
            self.redirect('/blog/%s' % str(p.key().id()))

        # Error handling if invalid post
        else:
            # Define error message to user
            error = "Subject and Content please :)"
            # Render HTML page with variables passed
            self.render("newpost.html", subject=subject, content=content, error=error)

class Rot13(Handler):
	""" Converts text into Ro13 """
	def get(self):
		# renders html form if get method is called
		self.render('rot13-form-custom.html')

	def post(self):
		Rot13 = ''
		text = self.request.get('text')
		# encode and decode text using built in rot13 functions 
		if text:
			rot13 = text.encode('rot13')

		# render HTML form and pass rot13 encoded text to text varilable
		self.render('rot13-form-custom.html', text = rot13)
		
# Define error handling functions

# Allow a-z, A-Z, 0-0, _, - using regular expression
# 3 - 20 characters
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

# Check password
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

# Check email
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return email and EMAIL_RE.match(email)

# Render welcome page if user has valid username, else redirect to signup
class NewWelcome(Handler):
    def get(self):
        if self.user:
            self.render('welcome.html', username = self.user.name)
        else:
            self.redirect('/signup')

class Welcome(Handler):
    def get(self):
        # Get username so we can use it as local var
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)
        else:
            self.redirect('/signup')

class Signup(Handler):

    # Render basic html page
    def get(self):
        self.render("blog-sign-up-form.html")

    # Post logic
    def post(self):
        # have_error var is used to determine if we should redirect or not
        have_error = False

        # get all vars (now calling self???)
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        # create dictionary for error handling
        params = dict(username = self.username,
                        email = self.email)

        # error handling
        if not valid_username(self.username):
            params['error_username'] = "Invalid username"
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "Invalid password"
            have_error = True

        elif self.password != self.verify:
            params['error_verify_password'] = "Passwords don't match"
            have_error = True

        if not valid_email(self.email):
            params['error_email'] = "Invalid email"
            have_error = True

        if have_error:
            self.render('blog-sign-up-form.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError

# remove this section?
class Unit2Signup(Signup):
    def done(self):
        self.redirect('/welcome?username=' + self.username)

class Register(Signup):
    def done(self):
        # make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists. '
            self.render('blog-sign-up-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog')

class Login(Handler):
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username,password)
        if u:
            self.login(u)
            self.redirect('/blog')
        else:
            msg = "Invalid login"
            self.render('login-form.html', error = msg)

class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', Rot13),
    ('/signup', Register),
    ('/welcome', Welcome),
    ('/blog/?', BlogFront),
    # Pass parameter into post page handler "+" means 1 or more numbers
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
    ('/cookies', Cookies),
    ('/login', Login),
    ('/logout', Logout),
    ('/NewWelcome', NewWelcome),
    ],
    debug=True)
