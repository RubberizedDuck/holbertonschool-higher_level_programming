#!/usr/bin/python3
"""
Script to list all states using SQLalchemy
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
    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
