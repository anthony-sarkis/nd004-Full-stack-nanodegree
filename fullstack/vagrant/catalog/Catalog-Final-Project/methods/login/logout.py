from flask import session as login_session
from flask import request, make_response, flash, redirect, url_for
from methods.login import gdisconnect, facebook
from methods import routes


@routes.route('/logout')
def logout():
    # Added Try/Except blocks to more smoothly handle variables not existing 
    # (ie logged in facebook not google)

    try:
        if login_session['provider_google'] == 'google':
            gdisconnect.gdisconnect()
            # This is an optimistic statement
            # TODO Add a success condition check?
            flash("Successfully logged out google.")
    except:
        pass
    
    try:
        if login_session['provider'] == 'facebook':
            facebook.fbdisconnect()
            flash("Successfully logged out facebook.")
    except:
        pass

    return redirect(url_for('routes.home'))
