#!/usr/bin/python3
""" Lists all State objects that contain the letter a
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    a_states = session.query(State).filter(State.name.like("%a%")).all()
    for state in a_states:
        print('{}: {}'. format(state.id, state.name))
    session.close()
