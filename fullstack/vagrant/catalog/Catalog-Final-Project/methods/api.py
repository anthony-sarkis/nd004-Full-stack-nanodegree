from flask import render_template, url_for, flash, request, redirect
from methods import routes


@routes.route('/api')
def api():
    return render_template('/api.html')
