#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
            'hbnb_dev',
            'hbnb_dev_pwd',
            'hbnb_dev_db'
        ), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

