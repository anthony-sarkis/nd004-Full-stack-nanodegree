from flask import render_template, flash
from . import routes
from helpers import antiforgery


@routes.route('/login')
def login():
    antiforgery.showLogin()
    return render_template('login.html')
