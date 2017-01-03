from flask import render_template, flash
from flask import session as login_session
from . import routes
from helpers import antiforgery


@routes.route('/login')
def login():
    state = antiforgery.secure()
    login_session['state'] = state
    return render_template('login.html', STATE=state)
