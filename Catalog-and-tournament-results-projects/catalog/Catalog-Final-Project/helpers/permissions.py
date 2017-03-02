from database_setup import Employer
from flask import session as login_session
from methods import userMethods
from helpers import sessionMaker

session = sessionMaker.newSession()

# True means has permission, False means doesn't.


def EmployerAdminAndLoggedIn(employer_id):
    employer = session.query(
        Employer).filter_by(id=employer_id).one()
    creator = userMethods.getUserInfo(employer.user_id)
    if 'username' in login_session and creator.id == login_session['user_id']:
        return True
    else:
        return False


def LoggedIn():
    if 'username' in login_session:
        return True
    else:
        return False
