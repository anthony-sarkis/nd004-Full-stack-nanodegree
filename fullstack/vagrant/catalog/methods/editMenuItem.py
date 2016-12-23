from flask import render_template, url_for, flash, request, redirect
from . import routes
from helpers import sessionMaker
from database_setup import MenuItem

session = sessionMaker.newSession()


@routes.route('/restaurants/<int:restaurant_id>/edit-menu-item/<int:menu_id>/',
              methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            editedItem.price = request.form['price']
            editedItem.description = request.form['description']
            editedItem.course = request.form['course']
            session.add(editedItem)
            session.commit()
            flash("You got it! Menu item updated.")
        return redirect(url_for('routes.showRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id,
            menu_id=menu_id, item=editedItem)


# Possible future functions
# Batch edit
# More advanced edit handling ie images
