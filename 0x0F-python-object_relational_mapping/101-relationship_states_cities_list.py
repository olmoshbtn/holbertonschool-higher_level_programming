#!/usr/bin/python3
"""
 Lists all State objects, and corresponding City objects,
 contained in the database hbtn_0e_101_usa
 """

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True
                )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        results = session.query(State)
        for state in results.order_by(State.id).all():
            print('{}: {}'.format(state.id, state.name))
            for city in state.cities:
                print('\t{}: {}'.format(city.id, city.name))
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
