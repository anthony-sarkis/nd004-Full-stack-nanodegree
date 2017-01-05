from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Category

session = sessionMaker.newSession()

"""

"""


@routes.route('/categories/new',
              methods=['GET', 'POST'])
def newCategory():
    # How can I use a try/except block better here?

    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])

        session.add(newCategory)
        session.commit()

        flash("Category created")

        return redirect(url_for('routes.viewAllCategories'))
    else:
        return render_template('newCategory.html')
