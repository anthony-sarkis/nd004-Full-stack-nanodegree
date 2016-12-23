from flask import Blueprint

routes = Blueprint('routes', __name__)

from .showRestaurants import showRestaurant, allRestaurants

from .editRestaurant import editRestaurant
from .deleteRestaurant import deleteRestaurant
from .newRestaurant import newRestaurant

from .deleteMenuItem import deleteMenuItem
from .newMenuItem import newMenuItem
from .editMenuItem import editMenuItem

from .home import home
