from flask import render_template, url_for, flash, request, redirect
from . import routes
from helpers import sessionMaker
from database_setup import Restaurant

session = sessionMaker.newSession()


@routes.route('/restaurant/<int:restaurant_id>/edit',
              methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            session.add(editedRestaurant)
            session.commit()
        flash("Restaurant updated.")
        return redirect(url_for('routes.showRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editrestaurant.html', restaurant_id=restaurant_id, restaurant=editedRestaurant)


# Possible future functions
# Batch edit
# More advanced edit handling ie images
