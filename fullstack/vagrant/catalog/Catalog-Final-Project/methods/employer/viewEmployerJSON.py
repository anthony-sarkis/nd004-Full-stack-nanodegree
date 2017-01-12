from flask import jsonify
from helpers import sessionMaker
from database_setup import Employer, Job
from methods import routes

session = sessionMaker.newSession()


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
