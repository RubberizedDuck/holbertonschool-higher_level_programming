#!/usr/bin/python3
"""
This module is designed to update the State name with id '2'
to 'New Mexico'
"""

from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy import update


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        update_state = session.query(State).filter(State.id == 2).first()
        update_state.name = 'New Mexico'
        session.commit()
