from flask import render_template, url_for, flash, request, redirect
from methods import routes
from methods.job import viewJob


@routes.route('/')
def home():
    recent_jobs = viewJob.viewRecentJobs()
    return render_template('/home/home.html', recent_jobs=recent_jobs)
