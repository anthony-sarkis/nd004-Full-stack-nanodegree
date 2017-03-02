#!/usr/bin/env python
import os
import webapp2
import jinja2
import re
from string import letters

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "html")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


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

        # get all vars
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        # create dictionary for error handling
        params = dict(username = username,
                        email = email)

        # error handling
        if not valid_username(username):
            params['error_username'] = "Invalid username"
            have_error = True

        if not valid_password(password):
            params['error_password'] = "Invalid password"
            have_error = True

        elif password != verify:
            params['error_verify_password'] = "Passwords don't match"
            have_error = True

        if not valid_email(email):
            params['error_email'] = "Invalid email"
            have_error = True

        if have_error:
            self.render('blog-sign-up-form.html', **params)
        else:
            self.redirect('/welcome?username=' + username)

app = webapp2.WSGIApplication([
    ('/', Rot13),
    ('/signup', Signup),
    ('/welcome', Welcome),
    ('/blog/?', BlogFront),
    # Pass parameter into post page handler "+" means 1 or more numbers
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
], debug=True)
