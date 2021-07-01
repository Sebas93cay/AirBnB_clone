#!/usr/bin/python3
"""This script contains the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class handle all the created object into a json file
    Attrs:
        __file_path (str): file name to save objects
        __objects (dict): dictionary of BaseModel objects
        classes (dict): dictionary of classes
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {'BaseModel': BaseModel, 'User': User, State: 'State',
               'City': City, 'Amenity': Amenity, 'Place': Place,
               'Review': Review}

    def all(self):
        """
        this returns all the objects
        """
        return self.__objects

    def new(self, obj):
        """This saves a new object into the __objects variable"""
        self.__objects[type(obj).__name__+'.'+str(obj.id)] = obj

    def reload(self):
        """
        This reads all the objects from the json file and
        save them into the __objects variable
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                tmp_dir = json.load(file)

            for k, v in tmp_dir.items():
                cls = self.classes[v['__class__']]
                self.__objects[k] = cls(**v)
        except:
            pass

    def save(self):
        """
        This functions rewrite the json file with the objects from
        the __objects variable
        """
        eldir = {}
        for k in self.__objects.keys():
            eldir[k] = self.__objects[k].to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(eldir, file)
