from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Job, Category
from helpers import permissions

session = sessionMaker.newSession()

"""
newJob function description:
On GET request: renders new item creation page.
On POST request: posts new item to database.
"""


@routes.route('/employer/<int:employer_id>/jobs/new',
              methods=['GET', 'POST'])
def newJob(employer_id):
    # How can I use a try/except block better here?

    categories = session.query(Category).all()

    if request.method == 'POST':
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            if request.form['header'] and request.form['salary'] and request.form['description'] and request.form['category']:
            
                category = session.query(Category).filter_by(
                    name=request.form['category']).one()

                newItem = Job(
                    header=request.form['header'],
                    salary=request.form['salary'],
                    description=request.form['description'],
                    category_id=category.id,
                    employer_id=employer_id)

                session.add(newItem)
                session.commit()
                flash("Hip hip hooray! Job created.")

                return redirect(url_for('routes.viewJob', job_id=newItem.id))
            else:
                flash("Please complete all fields.")
                # TODO save fields for user
                return render_template(
                '/job/newjob.html', employer_id=employer_id,
                categories=categories)
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))

    else:
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            return render_template(
                '/job/newjob.html', employer_id=employer_id,
                categories=categories)
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
