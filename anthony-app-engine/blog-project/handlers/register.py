import re
from handlers import handler
from models import user

# Define error handling functions for user creation
# Allow a-z, A-Z, 0-0, _, - using regular expression
# 3 - 20 characters
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


def valid_username(username):
    return username and USER_RE.match(username)


# Check password
def valid_password(password):
    return password and PASS_RE.match(password)


# Check email
def valid_email(email):
    return email and EMAIL_RE.match(email)
################


class Signup(handler.Handler):
    # Render basic html page
    def get(self):
        self.render("blog-sign-up-form.html")

    def post(self):
        # have_error var is used to determine if we should redirect or not
        have_error = False
        # pass html properties
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        # create dictionary for error handling
        params = dict(username=self.username, email=self.email)

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


# Registers a new user and logs them in. Handles errors by redireting.
class Register(Signup):
    def done(self):
        # make sure the user doesn't already exist
        u = user.User.by_name(self.username)
        if u:
            msg = 'That user already exists. '
            self.render('blog-sign-up-form.html', error_username=msg)
        else:
            u = user.User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/welcome')
