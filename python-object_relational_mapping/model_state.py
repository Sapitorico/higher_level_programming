#!/usr/bin/python3
"""Defines the State class and a Base instance for SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Return a string representation of the State object"""
        return "{}(name='{}')".format(self.__class__.__name__, self.name)
