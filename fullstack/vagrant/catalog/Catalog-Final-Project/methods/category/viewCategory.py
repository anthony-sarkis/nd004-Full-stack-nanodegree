from flask import render_template, jsonify, url_for, flash
from helpers import sessionMaker, permissions
from database_setup import Category, Job
from methods import routes
from flask import session as login_session
from methods.job import viewJob

session = sessionMaker.newSession()


# return all categories
@routes.route("/category/all")
def viewCategoryAll():

    recent_jobs = viewJob.viewRecentJobs()

    # categories = session.query(Job.category).distinct().all()
    categories = session.query(Category).all()
    # Permissions
    if permissions.LoggedIn() == True:
        return render_template('/category/viewCategoryAll.html',
                               categories=categories, recent_jobs=recent_jobs)
    else:
        return render_template('/category/viewCategoryAllPublic.html',
                               categories=categories, recent_jobs=recent_jobs)


# return a category
@routes.route("/category/<int:category_id>")
def viewCategory(category_id):

    # example of one to many
    category = session.query(Category).filter_by(id=category_id).one()
    jobs = session.query(Job).filter_by(category_id=category_id).all()

    # Permissions
    return render_template('/category/viewCategory.html', jobs=jobs, category=category)
