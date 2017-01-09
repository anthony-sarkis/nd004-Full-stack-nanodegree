from flask import render_template, jsonify, url_for, flash
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
                               employer=employer, jobs=jobs, employer_id=employer_id)
    else:
        return render_template('/employer/viewEmployerPublic.html',
                               employer=employer, jobs=jobs, employer_id=employer_id)

# return all employers


@routes.route("/employer/all")
def viewEmployerAll():
    employers = session.query(Employer).all()

    if permissions.LoggedIn() == True:
        return render_template('/employer/viewEmployerAll.html', employers=employers)
    else:
        return render_template('/employer/viewEmployerAllPublic.html', employers=employers)


# API endpoints
# Return all employers in JSON format
@routes.route("/employer/all/JSON")
def viewEmployerAllJSON():
    employers = session.query(Employer).all()
    return jsonify(Employers=[i.serialize for i in employers])


# Return a employer in JSON format
@routes.route("/employer/<int:employer_id>/JSON")
def viewEmployerJSON(employer_id):
    jobs = session.query(Job).filter_by(
        employer_id=employer_id).all()
    return jsonify(Jobs=[i.serialize for i in jobs])


# Return a job item in JSON format
@routes.route("/employer/<int:employer_id>/job/<int:job_id>/JSON")
def viewEmployerJobJSON(employer_id, job_id):
    item = session.query(Job).filter_by(id=job_id).one()
    return jsonify(Job=[item.serialize])
