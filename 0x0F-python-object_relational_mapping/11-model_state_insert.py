#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
