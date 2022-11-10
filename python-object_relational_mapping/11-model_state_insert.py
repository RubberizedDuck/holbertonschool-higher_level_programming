#!/usr/bin/python3
"""
This module is designed to add 'Louisiana' to State table
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
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        new_state = State(name='Louisiana')
        session.add(new_state)
