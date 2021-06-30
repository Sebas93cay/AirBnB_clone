#!/usr/bin/python3
"""This module define User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define User class inherint BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
