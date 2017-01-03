from flask import Blueprint

routes = Blueprint('routes', __name__)

# CRUD Restruants
from employer.viewEmployer import *
from employer.deleteEmployer import *
from employer.editEmployer import *
from employer.newEmployer import *

from job.editJob import *
from job.newJob import *
from job.deleteJob import *

from .home import *

# Login
from login.login import *
from login.logout import *

from login.gconnect import *
from login.gdisconnect import *
from login.facebook import *
