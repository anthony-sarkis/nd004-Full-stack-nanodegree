from flask import session as login_session
from flask import request, make_response, flash
from . import routes
from methods import gdisconnect, facebook


@routes.route('/logout')
def logout():
    # add method to handle if no login provider #buggy
    if login_session['provider']:

        if login_session['provider'] == 'google':
            gdisconnect.gdisconnect()
            # Add a if statement?
            output = "Successfully logged out google."

        if login_session['provider'] == 'facebook':
            facebook.fbdisconnect()
            output += "Successfully logged out facebook."

    else:
        output = "No Logins"

    # Redirect to home / handle better
    return output
