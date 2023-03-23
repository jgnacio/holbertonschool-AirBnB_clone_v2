#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from . import storage


class State(BaseModel, Base):
    """ State class s"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns the list of City.

            that contains instances with state_id equals to
            the current State.id.
            """
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
