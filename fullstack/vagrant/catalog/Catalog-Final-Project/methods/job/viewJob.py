from flask import render_template, flash, request
from methods import routes
from helpers import sessionMaker
from database_setup import Job

session = sessionMaker.newSession()


def viewRecentJobs():

    recent_jobs = session.query(Job).order_by(Job.id.desc()).limit(10)
    return recent_jobs


@routes.route('/job/<int:job_id>/view')
def viewJob(job_id):

    job = session.query(Job).filter_by(id=job_id).one()

    return render_template('/job/viewJob.html', job=job)


@routes.route('/jobs')
def viewJobAll():

    jobs = session.query(Job).all()

    recent_jobs = viewRecentJobs()

    return render_template('/job/viewJobAll.html',
                           jobs=jobs, recent_jobs=recent_jobs)
