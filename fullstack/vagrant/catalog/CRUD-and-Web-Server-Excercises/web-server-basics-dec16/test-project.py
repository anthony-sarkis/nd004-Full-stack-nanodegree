"""
12/22/2016

Code from Udacity training exercises.

After completing this I decided to refactor code into more abstract method files using bluepint.

Place back in to /catalog directory to test

"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# API Endpoints (GET Request)
# get menu
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

# get one specific menu item


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItems=[item.serialize])


@app.route('/')
def homepage():
    return "Welcome"


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    try:
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
        return render_template(
            'menu.html', restaurant=restaurant, items=items, restaurant_id=restaurant_id)
    except:
        return "No restaurant found"


@app.route('/restaurants/<int:restaurant_id>/new-menu-item/',
           methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # How can I use a try/except block better here?
    if request.method == 'POST':
        newItem = MenuItem(name=request.form[
            'name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("Now we are cooking! Menu item created.")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/edit-menu-item/<int:menu_id>/',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("You got it! Menu item updated.")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id,
            menu_id=menu_id, item=editedItem)


@app.route('/restaurants/<int:restaurant_id>/delete-menu-item/<int:menu_id>/',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    try:
        ItemToBeDeleted = session.query(MenuItem).filter_by(id=menu_id).one()
        if request.method == 'POST':
            session.delete(ItemToBeDeleted)
            session.commit()
            flash("Menu item? What menu item? Menu item deleted.")
            return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
        else:
            return render_template('deletemenuitem.html', item=ItemToBeDeleted)
    except:
        return "No item found"


if __name__ == '__main__':
    app.secret_key = 'so_secure'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
