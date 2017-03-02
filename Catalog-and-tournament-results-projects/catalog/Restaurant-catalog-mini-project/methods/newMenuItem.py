from flask import render_template, url_for, flash, request, redirect
from . import routes
from helpers import sessionMaker
from database_setup import MenuItem


session = sessionMaker.newSession()

"""
newMenuItem function description:
On GET request: renders new item creation page.
On POST request: posts new item to database.
"""


@routes.route('/restaurant/<int:restaurant_id>/new-menu-item',
              methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # How can I use a try/except block better here?
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'],
            price=request.form['price'],
            description=request.form['description'],
            course=request.form['course'],
            restaurant_id=restaurant_id)

        session.add(newItem)
        session.commit()
        flash("Now we are cooking! Menu item created.")
        return redirect(url_for('routes.showRestaurant',
                                restaurant_id=restaurant_id,
                                user_id=login_session['user_id']))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)
