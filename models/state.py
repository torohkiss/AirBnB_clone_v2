#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state", cascade="all, delete=orphan")
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            city_list = []
            all_cities = list(models.storage.all(City).values())
            for city in all_cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
