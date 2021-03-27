#!/usr/bin/python3
"""
 Changes the name of a State object from the database hbtn_0e_6_usa
 """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True
                )
        Session = sessionmaker(bind=engine)
        session = Session()

        match = session.query(State).filter(State.id == 2).first()

        if match is not None:
            match.name = 'New Mexico'
            session.commit()
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
