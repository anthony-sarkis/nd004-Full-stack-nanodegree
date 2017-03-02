from flask import render_template, url_for, flash
from helpers import sessionMaker
from database_setup import Employer, Job, Category
from methods import routes, userMethods
from flask import session as login_session
from helpers import permissions

session = sessionMaker.newSession()


# return a single employer
@routes.route("/employer/<int:employer_id>")
def viewEmployer(employer_id):
    employer = session.query(
        Employer).filter_by(id=employer_id).one()
    jobs = session.query(Job).filter_by(
        employer_id=employer_id).all()

    # Permissions
    if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
        return render_template('/employer/viewEmployer.html',
                               employer=employer, jobs=jobs,
                               employer_id=employer_id)
    else:
        return render_template('/employer/viewEmployerPublic.html',
                               employer=employer, jobs=jobs,
                               employer_id=employer_id)

# return all employers


@routes.route("/employer/all")
def viewEmployerAll():
    employers = session.query(Employer).all()

    if permissions.LoggedIn() == True:
        return render_template('/employer/viewEmployerAll.html', employers=employers)
    else:
        return render_template('/employer/viewEmployerAllPublic.html', employers=employers)



@routes.route("/employer/all/my")
def viewEmployerAllMy():
    
    creator = userMethods.getUserInfo(login_session['user_id'])
    employers = session.query(Employer).filter_by(user_id=creator.id).all()

    if permissions.LoggedIn() == True:
        return render_template('/employer/viewEmployerAllMy.html', employers=employers)
    else:
        return redirect()