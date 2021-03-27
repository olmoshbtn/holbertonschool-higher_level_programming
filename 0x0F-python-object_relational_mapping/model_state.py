#!/usr/bin/python3
"""
Class definition of a State and an instance Base using SQLAlchemy
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class State"""
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
