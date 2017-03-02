"""

Helper function that returns a session object

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base


def newSession():
    engine = create_engine('sqlite:///restaurantmenuwithusers.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
