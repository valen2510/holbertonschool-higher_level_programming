#!/usr/bin/python3
""" Change the name of a State object from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()
