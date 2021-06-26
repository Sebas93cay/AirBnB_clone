#!/usr/bin/python3
"""
This script contains the base model
"""

import uuid
from datetime import date, datetime
from models import storage


class BaseModel:
    """Base class to all other objects in the H_Air_BNB project"""

    def __init__(self, *args, **kwargs):
        """Init Base function"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs != {}:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if type(self.created_at) == str:
                self.created_at = datetime.strptime(
                    self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            if type(self.updated_at) == str:
                self.updated_at = datetime.strptime(
                    self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

        if 'id' not in kwargs.keys():
            storage.new(self)

    def __str__(self) -> str:
        """str function"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at instance variable to current time
        Save the instance into a json file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict returns a dictionary containing all keys/value of the
        instance. Aditionaly contains the '__class__' key with the name
        of the class and created_at and updated_at keys are converted
        to string object in ISO format %Y-%m-%dT%H:%M:%S.%f
        (ex: 2017-06-14T22:31:03.285259)
        """
        d = self.__dict__.copy()
        d['__class__'] = type(self).__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
