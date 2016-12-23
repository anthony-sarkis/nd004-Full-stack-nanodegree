from flask import render_template, url_for, flash, request, redirect
from . import routes


@routes.route('/')
def home():
    return render_template('home.html')
