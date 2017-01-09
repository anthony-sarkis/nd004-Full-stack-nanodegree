from flask import Blueprint

routes = Blueprint('routes', __name__)

# CRUD Restruants
from employer.viewEmployer import viewEmployer, viewEmployerAll, viewEmployerAllJSON, viewEmployerJSON, viewEmployerJobJSON
from employer.deleteEmployer import deleteEmployer
from employer.editEmployer import editEmployer
from employer.newEmployer import newEmployer

from job.editJob import editJob
from job.newJob import newJob
from job.deleteJob import deleteJob
from job.viewJob import viewJob, viewJobAll

from .home import home
from .api import api

# Login
from login.login import login
from login.logout import logout
from login.gconnect import gconnect, gconnectTest
from login.gdisconnect import gdisconnect
from login.facebook import fbconnect

from category.viewCategory import viewCategory, viewCategoryAll
from category.newCategory import newCategory
from category.deleteCategory import deleteCategory
