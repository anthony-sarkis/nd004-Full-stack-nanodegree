
import os
import webapp2
import jinja2
import re
import string
from helpers import hash_helpers
from google.appengine.ext import db
from models import user, post, comment

#from handlers import register
# Define HTML template directory, load templates using Jinja
# had as ".." prev in the handlers director
template_dir = os.path.join(os.path.dirname(__file__), '..', 'html')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def blog_key(name='default'):
    return db.Key.from_path('blogs', name)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


# Primary handler to help with general functions
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
        cookie_val = hash_helpers.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    # Request and verify cookie for user id
    def read_secure_cookie(self, name):
        # get cookie value
        cookie_val = self.request.cookies.get(name)
        # return value if it's secure?
        return cookie_val and hash_helpers.check_secure_val(cookie_val)

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
            self.user = uid and user.User.by_id(int(uid))

    # Create key. Find post from post_id
    # Call int to transform string from URL into integer post ID        
    def get_post_key(self, post_id):
        x = db.Key.from_path('Post', int(post_id), parent=blog_key())
        return x

    # Use to get a user ID from cookies to see who is making the post.
    def getUserID(self):
        # Is this right?
        x = self.read_secure_cookie('user_id')
        # return if cookie is blank, otherwise return value
        if not x == '':
            x = int(x.split('|')[0])
            return x

def render(self, Handler):
    # Replace line break with html <br> to render well
    self.render_text = self.content.replace('\n', '<br>')
    return render_str("post.html", p=self)