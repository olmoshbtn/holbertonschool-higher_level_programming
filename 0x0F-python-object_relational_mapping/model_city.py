#!/usr/bin/python3
"""
Class definition of a City and an instance Base using SQLAlchemy
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class State"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
    name = Column(
        String(256),
        nullable=False,
    )
