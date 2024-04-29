#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy import Table, Column, Integer, String, create_engine

Base = declarative_base()

class State(Base):
    """
    this state class inherits from Base
    """

    __tablename__ = "state"
    id = Column(Integer, nullable=False, priamary_key=True,
            autoincreament=True, unique=True)
    name = Column(String(128), nullable=False)
