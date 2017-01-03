from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Job


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
    if request.method == 'POST':
        newItem = Job(
            header=request.form['header'],
            salary=request.form['salary'],
            description=request.form['description'],
            category=request.form['category'],
            employer_id=employer_id)

        session.add(newItem)
        session.commit()
        flash("Now we are cooking! Menu item created.")
        return redirect(url_for('routes.showRestaurant',
                                employer_id=employer_id,
                                user_id=login_session['user_id']))
    else:
        return render_template('newjob.html', employer_id=employer_id)
