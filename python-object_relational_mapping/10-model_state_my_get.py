#!/usr/bin/python3
''' script that prints the State\\
    object with the name passed as\\
        argument from the database hbtn_0e_6_usa'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if (__name__ == "__main__"):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            session.close()
            exit()

    print("Not found")
    session.close()
