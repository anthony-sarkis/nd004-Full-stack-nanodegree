#!/usr/bin/env python
import os
import webapp2
import jinja2
import re
import hashlib
import hmac
import string
import random
from string import letters
from google.appengine.ext import db

# Define HTML template directory, load templates using Jinja
template_dir = os.path.join(os.path.dirname(__file__), "html")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

# #################### Hashing and password functions

# normally would not store in this file
SECRET = 'imsosecret'

# call hmac passing secret phrase and phrase variable
def hash_str(s):
    x = hmac.new(SECRET,s).hexdigest()
    return x

# Return string with hash and value
def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

# Check if cookie hash value equals real hash
def check_secure_val(h): 
    x = h.split('|')[0]
    if make_secure_val(x) == h:
        return x

# Salt for password hash 
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# Make password hash
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

# Class for Users
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
        # Calls class method by name pass name
        u = cls.by_name(name)
        # check if user has valid password
        if u and valid_pw(name, pw, u.pw_hash):
            return u


###############################

# Primary handler
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

    # calls make secure val, and sets cookie
    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    # Request and verify cookie for user id
    def read_secure_cookie(self, name):
        # get cookie value
        cookie_val = self.request.cookies.get(name)
        # return value if it's secure?
        return cookie_val and check_secure_val(cookie_val)

    # Login user by setting a secure cookie, passing user ID
    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    # Log user out by setting Cookie to = nothing, use path to control pages
    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    # Runs on every request to see if user is logged in or not.
    def initialize(self, *a, **kw):
            webapp2.RequestHandler.initialize(self, *a, **kw)
            uid = self.read_secure_cookie('user_id')
            self.user = uid and User.by_id(int(uid))

    def getUserID(self):
        x = self.read_secure_cookie('user_id')
        x = int(x.split('|')[0])
        return x 

# Blog section   ###############

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

# render all posts blog front page
class BlogFront(Handler):
    def get(self):
        # Get posts from DB. Select all from Post table order by created
        posts = greetings = Post.all().order('-created')
        # Render front page, pass "posts" variable as posts
        self.render('front.html', posts = posts)

# Class for post creation
class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    # Used to assign a post to a user
    created_by = db.IntegerProperty(required = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        # Replace line break with html <br> to render well
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)

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
    """ """
    # Render new post HTML
    def get(self):
        self.render("newpost.html")

    # On Post render
    def post(self):
        # Get variables passed from form
        subject = self.request.get('subject')
        content = self.request.get('content')
        # assign post to a user using getUserbyID method
        created_by = self.getUserID()

        # Handle if valid post
        if subject and content:
            # Create new post as p variable
            p = Post(parent = blog_key(), subject=subject, content=content, created_by=created_by)
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

#### NEW  ############ INCOMPLETE as of 9/27

class EditPost(Handler):
    def get(self, post_id):
        # Create key. Find post from post_id
        # Call int to transform string from URL into integer post ID
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # Look up a specific item in the db using key
        post = db.get(key)
        ### Need to figure out right way to access POST datastore attributes.
        content = self.post.content
        subject = self.post.subject

        # Return error if no valid key
        if not post:
            self.error(404)
            return

        # Render page using Permalink HTML as a template, pass post var as post
        self.render("editpost.html", content=content, subject=subject)

    def post(self):
        # Get variables passed from form
        subject = self.request.get('subject')
        content = self.request.get('content')
        key = self.post.blog_key
        # assign post to a user using getUserbyID method
        created_by = self.getUserID()

        # Handle if valid post
        if subject and content:
            # Create new post as p variable
            p = Post(blog_key=key, subject=subject, content=content, created_by=created_by)
            # Store element (p) in database
            p.put()
            # Redirect to blog page using ID of element
            self.redirect('/blog/%s' % str(p.key().id()))

        # Error handling if invalid post
        else:
            # Define error message to user
            error = "Subject and Content please :)"
            # Render HTML page with variables passed
            self.render("editpost.html", subject=subject, content=content, error=error)
########### INCOMPLETE as of 9/27
	

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
################


# Displays welcome page if valid user
class Welcome(Handler):
    def get(self):
        if self.user:
            # Calling class function to look up username by name
            self.render('welcome.html', username = self.user.name)
        else:
            self.redirect('/signup')

class Signup(Handler):
    # Render basic html page
    def get(self):
        self.render("blog-sign-up-form.html")
    # 
    def post(self):
        # have_error var is used to determine if we should redirect or not
        have_error = False
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

# Register calling signup class
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
            self.redirect('/welcome')

""" 
Login control flow

1. Get's username and password from form
2. Creates a varible "u" using class method User.login
    2.1 User.login calls @ClassMethod by_name, which filters all users where name = user
    2.2 Runs valid_pw to check if password hash is valid, returns u if so
3. Calls self.login method pass "u" variable
    3.1 This sets a secure cookie.
"""

class Login(Handler):
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/welcome')
        else:
            msg = "Invalid login"
            self.render('login-form.html', error = msg)

class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/signup')

app = webapp2.WSGIApplication([
    ('/', Register),
    ('/signup', Register),
    ('/welcome', Welcome),
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
    ('/login', Login),
    ('/logout', Logout),
    ('/edit/([0-9]+)', EditPost),
    ],
    debug=True)
