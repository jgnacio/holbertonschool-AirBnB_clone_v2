#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import classes


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)

    def all(self, cls=None):
        """Returns all instances of the given class."""
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(classes['State']).all()
            objs.extend(self.__session.query(classes['City']).all())
            objs.extend(self.__session.query(classes['User']).all())
            objs.extend(self.__session.query(classes['Place']).all())
            objs.extend(self.__session.query(classes['Review']).all())
            objs.extend(self.__session.query(classes['Amenity']).all())
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def delete(self, obj=None):
        """Delete a given object."""
        if obj is not None:
            self.__session.delete(obj)

    def new(self, obj):
        """Create a new objet."""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        mkrsession = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(mkrsession)
        self.__session = Session()

    def close(self):
        self.__session.close()
