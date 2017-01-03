from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Employer

session = sessionMaker.newSession()


@routes.route('/employer/<int:employer_id>/edit',
              methods=['GET', 'POST'])
def editEmployer(employer_id):
    i = session.query(
        Employer).filter_by(id=employer_id).one()
    if request.method == 'POST':
        if request.form['name']:
            i.name = request.form['name']
            session.add(i)
            session.commit()
        flash("Employer updated.")
        return redirect(url_for('routes.viewSingleEmployer', employer_id=employer_id))
    else:
        return render_template(
            'editemployer.html', employer_id=employer_id, employer=i)


# Possible future functions
# Batch edit
# More advanced edit handling ie images
