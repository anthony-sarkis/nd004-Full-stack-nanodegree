"""
Main entry point for application.
"""

from flask import Flask, Blueprint, render_template, abort
from methods import *

app = Flask(__name__)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.secret_key = 'so_secure'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
