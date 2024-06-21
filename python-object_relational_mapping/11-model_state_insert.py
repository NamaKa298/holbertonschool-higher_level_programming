#!/usr/bin/python3
'''script that adds the State object “Louisiana”\\
    to the database hbtn_0e_6_usa'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if (__name__ == "__main__"):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    nouveau_pays = State(name="Louisiana")
    session.add(nouveau_pays)
    session.commit()
    print(nouveau_pays.id)
    session.close()
