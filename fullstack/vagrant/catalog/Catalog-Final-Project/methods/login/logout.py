from flask import session as login_session
from flask import request, make_response, flash
from methods import gdisconnect, facebook, routes


@routes.route('/logout')
def logout():
    # add method to handle if no login provider #buggy
    output = ""

    if login_session['provider_google'] == 'google':
        gdisconnect.gdisconnect()
        # Add a if statement?
        output += "Successfully logged out google."

    elif login_session['provider_facebook'] == 'facebook':
        facebook.fbdisconnect()
        output += "Successfully logged out facebook."
    else:
        output += "Nothing to logout"

    # Redirect to home / handle better
    return output
