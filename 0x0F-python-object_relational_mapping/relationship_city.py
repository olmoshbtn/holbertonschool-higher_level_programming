#!/usr/bin/python3
"""
Class definition of a City and an instance Base using SQLAlchemy
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class City"""
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
        ForeignKey('states.id'),
        nullable=False,
    )
    name = Column(
        String(256),
        nullable=False,
    )
