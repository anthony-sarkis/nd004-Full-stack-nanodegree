"""
Functions related to deleting employers
"""

from flask import render_template, url_for, flash, request, redirect
from methods import routes  # Blueprint routes from __init__.py
from helpers import sessionMaker
from database_setup import Employer

session = sessionMaker.newSession()


"""
deleteEmployer function description:
On GET request: renders delete confirmation page.
On POST request: deletes employer and updates user.
"""


@routes.route('/employer/<int:employer_id>/delete',
              methods=['GET', 'POST'])
def deleteEmployer(employer_id):
    i = session.query(
        Employer).filter_by(id=employer_id).one()
    if request.method == 'POST':
        session.delete(i)
        session.commit()
        flash("Employer deleted.")
        return redirect(url_for('routes.viewEmployerAll'))
    else:
        return render_template('/employer/deleteEmployer.html', employer_id=employer_id,
                               employer=i)


# Potential future functions
# Soft delete for recovery
# Hide/show concept (this could be in edit too)
# Batch delete maybe
