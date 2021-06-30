#!/usr/bin/python3
"""This module define Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Define Place class inherint BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
