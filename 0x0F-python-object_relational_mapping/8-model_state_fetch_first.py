#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    first_row = session.query(State).first()
    if first_row:
        print('{}: {}'.format(first_row.id, first_row.name))
    else:
        print("Nothing")
    session.close()
