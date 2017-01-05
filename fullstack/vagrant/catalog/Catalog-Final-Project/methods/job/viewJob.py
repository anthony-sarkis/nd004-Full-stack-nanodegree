from flask import render_template, flash, request
from methods import routes
from helpers import sessionMaker
from database_setup import Job

session = sessionMaker.newSession()


@routes.route('/job/<int:job_id>/view')
def viewJob(job_id):

    job = session.query(Job).filter_by(id=job_id).one()

    return render_template('viewJob.html', job=job)


@routes.route('/jobs')
def viewAllJobs():

    jobs = session.query(Job).all()

    return render_template('viewAllJobs.html', jobs=jobs)
