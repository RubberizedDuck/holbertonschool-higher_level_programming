#!/usr/bin/python3
"""
This module is designed to return the state id
from what the user inputs in argv[4]
"""

from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    user_input = argv[4]
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker()

    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like(user_input)).first()
    if not state:
        print('Not found')
    else:
        print(f'{state.id}')
