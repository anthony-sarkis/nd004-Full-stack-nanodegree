from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Employer
from flask import session as login_session

session = sessionMaker.newSession()


@routes.route('/employer/new', methods=['GET', 'POST'])
def newEmployer():
    if request.method == 'POST':

        # TO DO review permissions

        # user must be logged in to acccess page in general and user_id

        ######

        newEmployer = Employer(name=request.form['name'],
                               user_id=login_session['user_id'])
        session.add(newEmployer)
        session.commit()
        flash("Welcome! Employer created.")
        employer_id = newEmployer.id
        return redirect(url_for('routes.viewEmployer',
                                employer_id=employer_id))
    else:
        return render_template('/employer/newEmployer.html')
