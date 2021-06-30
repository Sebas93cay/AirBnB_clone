#!/usr/bin/python3
"""This module define Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define State Review inherint BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
