#!/usr/bin/python3
'''script that lists all State objects from the database hbtn_0e_6_usa'''

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2],
    sys.argv[3]), pool_pre_ping=True)
session = Session(engine)
Base.metadata.create_all(engine)

all_states = session.query(State).all()

for state in all_states:
    print("{}: {}".format(state.id, state.name))
