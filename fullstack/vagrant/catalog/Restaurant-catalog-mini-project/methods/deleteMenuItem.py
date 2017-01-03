"""
Functions related to deleting menu items
"""

from flask import render_template, url_for, flash, request, redirect
from . import routes  # Blueprint routes from __init__.py
from helpers import sessionMaker
from database_setup import MenuItem

session = sessionMaker.newSession()


"""
deleteMenuItem function description:
On GET request: renders delete confirmation page.
On POST request: deletes a menu item and updates user.
"""


@routes.route('/restaurant/<int:restaurant_id>/delete-menu-item/<int:menu_id>/',
              methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    ItemToBeDeleted = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(ItemToBeDeleted)
        session.commit()
        flash("Menu item? What menu item? Menu item deleted.")
        return redirect(url_for('routes.showRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=ItemToBeDeleted)


# Potential future functions
# Soft delete for recovery
# Hide/show concept (this could be in edit too)
# Batch delete maybe
