#!/usr/bin/python3
"""
Provides a State class to map to objects in a states table
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Representation of a State
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    name = Column(
        String(128),
        nullable=False,
    )
    cities = relationship(
        'City', backref='state', cascade='all, delete-orphan'
        )
