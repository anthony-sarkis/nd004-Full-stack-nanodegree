from flask import session as login_session
import random
import string


def showLogin():
    salt = 'apple2'
    state = ''.join(random.choice(string.ascii_uppercase + string.digits
                                  + salt) for x in xrange(32))
    login_session['state'] = state
    return "The current state is %s" % login_session
