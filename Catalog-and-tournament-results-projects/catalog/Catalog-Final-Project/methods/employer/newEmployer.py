from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Employer
from flask import session as login_session
from helpers import permissions

session = sessionMaker.newSession()


@routes.route('/employer/new', methods=['GET', 'POST'])
def newEmployer():
    if request.method == 'POST':
        if permissions.LoggedIn() == True:
            if request.form['name']:
                newEmployer = Employer(name=request.form['name'],
                                   user_id=login_session['user_id'])
                session.add(newEmployer)
                session.commit()
                flash("Welcome! Employer created.")
                employer_id = newEmployer.id
                return redirect(url_for('routes.viewEmployer',
                                        employer_id=employer_id))
            else:
                flash("Name please")
            return redirect(url_for('routes.newEmployer'))
        else:
            flash("Please login to create an employer")
            return redirect(url_for('routes.newEmployer'))
    # GET request
    else:
        if permissions.LoggedIn() == True:
            return render_template('/employer/newEmployer.html')
        else:
            flash("Please login to create an employer")
            return redirect(url_for('routes.viewEmployerAll'))
