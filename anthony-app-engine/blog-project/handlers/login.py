from handlers import handler
from models import user

""" 
Login control flow

1. Get's username and password from form
2. Creates a varible "u" using class method User.login
    2.1 User.login calls @ClassMethod by_name, which filters all users where name = user
    2.2 Runs valid_pw to check if password hash is valid, returns u if so
3. Calls self.login method pass "u" variable
    3.1 This sets a secure cookie.
"""


class Login(handler.Handler):
    def get(self):
        error = self.request.get('error')
        self.render('login-form.html', error=error)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = user.User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/welcome')
        else:
            msg = "Invalid login"
            self.render('login-form.html', error=msg)