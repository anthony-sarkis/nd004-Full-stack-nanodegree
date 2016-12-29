from flask import Blueprint

routes = Blueprint('routes', __name__)

# CRUD Restruants
from .showRestaurants import showRestaurant, allRestaurants
from .editRestaurant import editRestaurant
from .deleteRestaurant import deleteRestaurant
from .newRestaurant import newRestaurant

# CUD  Menu items
from .deleteMenuItem import deleteMenuItem
from .newMenuItem import newMenuItem
from .editMenuItem import editMenuItem

# Home
from .home import home

# Login
from .login import login
from .gconnect import gconnect, gconnectTest
from .gdisconnect import gdisconnect
from .facebook import fbconnect, fbdisconnect
