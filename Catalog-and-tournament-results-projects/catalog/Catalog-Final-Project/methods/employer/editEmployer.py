from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Employer
from helpers import permissions

session = sessionMaker.newSession()


@routes.route('/employer/<int:employer_id>/edit',
              methods=['GET', 'POST'])
def editEmployer(employer_id):
    i = session.query(
        Employer).filter_by(id=employer_id).one()
    if request.method == 'POST':
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            if request.form['name']:
                i.name = request.form['name']
                session.add(i)
                session.commit()
                flash("Employer updated.")
                return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
    # Get request
    else:
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            return render_template(
                '/employer/editEmployer.html', employer_id=employer_id,
                employer=i)
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))


# Possible future functions
# Batch edit
# More advanced edit handling ie images
