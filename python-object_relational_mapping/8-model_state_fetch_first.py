#!/usr/bin/python3
"""
This module is designed to return the first state
in the database
"""

from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker()

    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).first()
    if not state:
        print('Nothing')
    else:
        print(f'{state.id}: {state.name}')
