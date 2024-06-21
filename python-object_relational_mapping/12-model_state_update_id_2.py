#!/usr/bin/python3
'''script that changes the name of a\\
    State object from the database hbtn_0e_6_usa'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if (__name__ == "__main__"):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
