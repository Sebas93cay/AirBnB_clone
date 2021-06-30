#!/usr/bin/python3
"""This module define User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define User class inherint BaseModel
    Attrs:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first_name of the user
        last_name = (str): last_name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
