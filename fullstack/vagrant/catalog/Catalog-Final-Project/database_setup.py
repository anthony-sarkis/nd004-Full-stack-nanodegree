import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Employer(Base):
    __tablename__ = 'employer'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # returns object data in easy serializable format
        # Description : variable
        return {
            'name': self.name,
            'id': self.id,
        }


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    header = Column(String(80), nullable=False)
    description = Column(String(80))
    salary = Column(String(8))
    category = Column(String(250))
    employer_id = Column(Integer, ForeignKey('employer.id'))
    employer = relationship(Employer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # returns object data in easy serializable format
        # Description : variable
        return {
            'header': self.header,
            'description': self.description,
            'id': self.id,
            'salary': self.salary,
            'category': self.category,
        }


#### insert at end of file ###
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
