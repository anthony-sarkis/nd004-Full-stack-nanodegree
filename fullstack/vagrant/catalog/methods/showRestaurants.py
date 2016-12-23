from flask import render_template, jsonify, url_for, flash
from . import routes
from helpers import sessionMaker
from database_setup import Restaurant, MenuItem

session = sessionMaker.newSession()


# return a single restaurant
@routes.route("/restaurant/<int:restaurant_id>")
def showRestaurant(restaurant_id):
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant,
                           items=items, restaurant_id=restaurant_id)


# return all restaurants
@routes.route("/restaurants")
def allRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('allrestaurants.html', restaurants=restaurants)


# API endpoints
# Return all restaurants in JSON format
@routes.route("/restaurants/JSON")
def allRestaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants])


# Return a restaurant in JSON format
@routes.route("/restaurant/<int:restaurant_id>/JSON")
def showRestaurantJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


# Return a menu item in JSON format
@routes.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON")
def showRestaurantMenuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=[item.serialize])
