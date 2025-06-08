#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review
import os

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref="place", cascade="all, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity, 
                                 viewonly=False, backref="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            review_list = []
            all_reviews = list(models.storage.all(Review).values())
            for review in all_reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        @property
        def amenities(self):
            """Returns the list of Amenity instances based on amenity_ids"""
            amenity_list = []
            all_amenities = list(models.storage.all(Amenity).values())
            for amenity in all_amenities:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity.id to the amenity_ids attribute"""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
