#!/usr/bin/python3
"""This script contains the FileStorage class"""

import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__+'.'+str(obj.id)] = obj

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                tmp_dir = json.load(file)
            for k, v in tmp_dir.items():
                self.__objects[k] = BaseModel(**v)
        except:
            pass

    def save(self):
        eldir = {}
        for k in self.__objects.keys():
            eldir[k] = self.__objects[k].to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(eldir, file)
