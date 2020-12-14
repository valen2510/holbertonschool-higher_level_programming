#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    element = session.query(State).filter(State.name == argv[4]).first()
    if element:
            print('{}'.format(element.id))
    else:
        print('Not found')
    session.close()
