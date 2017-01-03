from flask import render_template, url_for, flash, request, redirect
from methods import routes


@routes.route('/')
def home():
    return render_template('home.html')
