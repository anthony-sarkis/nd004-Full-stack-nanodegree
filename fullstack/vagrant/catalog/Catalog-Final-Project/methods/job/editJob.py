from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Job

session = sessionMaker.newSession()


@routes.route('/employers/<int:employer_id>/jobs/<int:job_id>/edit',
              methods=['GET', 'POST'])
def editJob(employer_id, job_id):
    i = session.query(Job).filter_by(id=job_id).one()
    if request.method == 'POST':
        if request.form['header']:
            i.header = request.form['header']
            i.salary = request.form['salary']
            i.description = request.form['description']
            i.category = request.form['category']
            session.add(i)
            session.commit()
            flash("You got it! Job updated.")
        return redirect(url_for('routes.viewSingleEmployer', employer_id=employer_id))
    else:
        return render_template(
            'editjob.html', employer_id=employer_id,
            job_id=job_id, job=i)


# Possible future functions
# Batch edit
# More advanced edit handling ie images
