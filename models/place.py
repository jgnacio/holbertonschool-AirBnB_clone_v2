#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id",
           String(60),
           ForeignKey("places.id"),
           primary_key=True,
           nullable=False),
    Column("amenity_id",
           String(60),
           ForeignKey("amenities.id"),
           primary_key=True,
           nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="places", cascade="delete")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False
        )
    else:

        @property
        def reviews(self):
            """Returns list of reviews associated with place"""
            from models import storage
            my_list = []
            for i in storage.all(Review):
                if self.id == i.place_id:
                    my_list.append(i)
            return my_list

        @property
        def amenities(self):
            """Returns list of amenities associated with place"""
            from models import storage
            my_list = []
            for i in storage.all(Amenity).values():
                if i.id in self.amenity_ids:
                    my_list.append(i)
            return my_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
