from flask import render_template, url_for, flash, request, redirect
from . import routes
from helpers import sessionMaker
from database_setup import Restaurant

session = sessionMaker.newSession()


@routes.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'],
                                   user_id=login_session['user_id'])
        session.add(newRestaurant)
        session.commit()
        flash("Now we are cooking! Restaurant created.")
        restaurant_id = newRestaurant.id
        return redirect(url_for('routes.showRestaurant',
                                restaurant_id=restaurant_id))
    else:
        return render_template('newRestaurant.html')
