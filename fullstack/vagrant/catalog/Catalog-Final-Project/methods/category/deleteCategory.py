from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Category

session = sessionMaker.newSession()

"""

"""


@routes.route('/category/<int:category_id>/delete',
              methods=['GET', 'POST'])
def deleteCategory(category_id):
    category = session.query(
        Category).filter_by(id=category_id).one()

    if request.method == 'POST':
        session.delete(category)
        session.commit()
        flash("Category deleted")
        return redirect(url_for('routes.viewAllCategories'))

    else:
        return render_template('/category/deleteCategory.html', category=category)
