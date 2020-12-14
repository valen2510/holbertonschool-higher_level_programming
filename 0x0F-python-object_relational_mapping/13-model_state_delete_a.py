#!/usr/bin/python3
""" Deletes all State objects with a name
    containing the letter a from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session='fetch')
    session.commit()
    session.close()
