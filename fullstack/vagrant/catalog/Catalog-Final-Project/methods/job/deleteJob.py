"""
Functions related to deleting menu jobs
"""

from flask import render_template, url_for, flash, request, redirect
from methods import routes  # Blueprint routes from __init__.py
from helpers import sessionMaker
from database_setup import Job

session = sessionMaker.newSession()


"""
deleteJob function description:
On GET request: renders delete confirmation page.
On POST request: deletes a menu job and updates user.
"""


@routes.route('/employer/<int:employer_id>/jobs/<int:job_id>/delete',
              methods=['GET', 'POST'])
def deleteJob(employer_id, job_id):
    i = session.query(Job).filter_by(id=job_id).one()
    if request.method == 'POST':
        session.delete(i)
        session.commit()
        flash("Job? What  job? Menu job deleted.")
        return redirect(url_for('routes.showRestaurant', employer_id=employer_id))
    else:
        return render_template('deletejob.html', job=i)


# Potential future functions
# Soft delete for recovery
# Hide/show concept (this could be in edit too)
# Batch delete maybe
