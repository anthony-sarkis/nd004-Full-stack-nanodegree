from flask import render_template, jsonify, url_for, flash
from helpers import sessionMaker
from database_setup import Category, Job
from methods import routes
from flask import session as login_session

session = sessionMaker.newSession()


# return all categories
@routes.route("/categories")
def viewAllCategories():
    # categories = session.query(Job.category).distinct().all()
    categories = session.query(Category).all()
    # Permissions
    if 'username' not in login_session:
        return render_template('viewCategories-private.html', categories=categories)
    else:
        return render_template('viewCategories-private.html', categories=categories)


# return a category
@routes.route("/category/<int:category_id>")
def viewCategory(category_id):

    # example of one to many
    category = session.query(Category).filter_by(id=category_id).one()

    jobs = session.query(Job).filter_by(category_id=category_id).all()

    # Permissions
    if 'username' not in login_session:
        return render_template('viewCategory-private.html', jobs=jobs, category=category)
    else:
        return render_template('viewCategory-private.html', jobs=jobs, category=category)
