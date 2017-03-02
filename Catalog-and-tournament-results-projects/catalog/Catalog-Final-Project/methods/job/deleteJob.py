"""
Functions related to deleting jobs
"""

from flask import render_template, url_for, flash, request, redirect
from methods import routes  # Blueprint routes from __init__.py
from helpers import sessionMaker
from database_setup import Job
from helpers import permissions

session = sessionMaker.newSession()


"""
deleteJob function description:
On GET request: renders delete confirmation page.
On POST request: deletes a menu job and updates user.
"""


@routes.route('/employer/<int:employer_id>/job/<int:job_id>/delete',
              methods=['GET', 'POST'])
def deleteJob(employer_id, job_id):
    i = session.query(Job).filter_by(id=job_id).one()
    if request.method == 'POST':
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            session.delete(i)
            session.commit()
            flash("Job? What  job? Job deleted.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
    else:
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            return render_template('/job/deletejob.html', job=i)
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer', employer_id=employer_id))


# Potential future functions
# Soft delete for recovery
# Hide/show concept (this could be in edit too)
# Batch delete maybe
