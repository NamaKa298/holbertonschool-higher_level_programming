#!/usr/bin/python3

'''Contains the class definition of a\\
    State and an instance Base = declarative_base()'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
import sys

Base = declarative_base()

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]
), pool_pre_ping=True)


class State(Base):
    '''creation de la classe State qui herite de Base'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))


Base.metadata.create_all(engine)
