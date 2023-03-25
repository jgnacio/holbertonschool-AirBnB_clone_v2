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
        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Returns all instances of the given class."""
        from models.base_model import BaseModel

        new_dict = {}

        if cls is None:
            for class_name in classes.values():
                if class_name != classes["BaseModel"]:
                    for obj in self.__session.query(class_name).all():
                        new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for obj in self.__session.query(cls).all():
                new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return new_dict

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
        self.__session = scoped_session(sessionmaker(self.__engine, expire_on_commit=False))
