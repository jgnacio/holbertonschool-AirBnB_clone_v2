#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @ property
        def cities(self):
            """Return all cities linked to this relationship."""
            from models import storage
            my_list = []
            for i in list(storage.all(City).values()):
                if self.id == i.state_id:
                    my_list.append(i)
            return my_list
