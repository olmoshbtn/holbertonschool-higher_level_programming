#!/usr/bin/python3
"""
 Lists all City objects from the database hbtn_0e_101_usa
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

        results = session.query(City, State).filter(City.state_id == State.id)
        for city, state in results.order_by(City.id).all():
            print('{}: {} -> {}'.format(city.id, city.name, state.name))
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
