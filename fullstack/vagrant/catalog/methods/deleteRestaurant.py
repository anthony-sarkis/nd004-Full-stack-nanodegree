"""
Functions related to deleting restaurants
"""

from flask import render_template, url_for, flash, request, redirect
from . import routes  # Blueprint routes from __init__.py
from helpers import sessionMaker
from database_setup import Restaurant

session = sessionMaker.newSession()


"""
deleteRestaurant function description:
On GET request: renders delete confirmation page.
On POST request: deletes restaurant and updates user.
"""


@routes.route('/restaurant/<int:restaurant_id>/delete',
              methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToBeDeleted = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToBeDeleted)
        session.commit()
        flash("Restaurant deleted.")
        return redirect(url_for('routes.home'))
    else:
        return render_template('deleterestaurant.html', restaurant_id=restaurant_id,
                               restaurant=restaurantToBeDeleted)


# Potential future functions
# Soft delete for recovery
# Hide/show concept (this could be in edit too)
# Batch delete maybe
