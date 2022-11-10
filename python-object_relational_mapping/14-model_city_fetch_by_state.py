#!/usr/bin/python3
"""
This module is designed to fetch all States and Cities by their id
and return the State with the city id and city name
"""

from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy import update


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    fetch_states = session.query(
        City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in fetch_states:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()
