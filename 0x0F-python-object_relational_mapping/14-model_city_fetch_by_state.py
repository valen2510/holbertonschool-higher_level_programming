#!/usr/bin/python3
""" Prints all City objects from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import City

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    tables = session.query(State, City).join(City).all()
    for state, city in tables:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
