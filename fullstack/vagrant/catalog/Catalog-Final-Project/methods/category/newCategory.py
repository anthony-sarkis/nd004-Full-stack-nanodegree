from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker, permissions
from database_setup import Category

session = sessionMaker.newSession()

"""

"""


@routes.route('/category/new',
              methods=['GET', 'POST'])
def newCategory():
    # How can I use a try/except block better here?
    if permissions.LoggedIn() == True:
        if request.method == 'POST':
            if request.form['name']:
                newCategory = Category(name=request.form['name'])

                session.add(newCategory)
                session.commit()

                flash("Category created")
                return redirect(url_for('routes.viewCategoryAll'))
            else:
                flash("Category please")
                return render_template('/category/newCategory.html')
        else:
            return render_template('/category/newCategory.html')
    else:
        flash("Please login to create a category")
        return redirect(url_for('routes.home'))
