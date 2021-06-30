#!/usr/bin/python3
"""unittests for file_storage.py"""
import os
import json
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""


    def setUp(self):
        if os.path.isfile('file.json'):
            os.remove('file.json')
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.isfile('file.json'):
            os.remove('file.json')
        FileStorage._FileStorage__objects = {}

    def test_fileStorage_from_models(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_fileStorage_init_args(self):
        with self.assertRaises(TypeError):
            FileStorage("12345")
            FileStorage(1234)
            FileStorage([])
            FileStorage({})
            FileStorage(None)

    def test_fileStorage_attrs(self):
        with self.assertRaises(AttributeError):
            models.storage.file_path
            models.storage.objects

    def test_fileStorage_all(self):
        self.assertEqual(type(models.storage.all()), dict)
        self.assertEqual(len(models.storage.all()), 0)
        models.storage.new(BaseModel())
        self.assertEqual(len(models.storage.all()), 1)

    def test_fileStorage_all_args(self):
        with self.assertRaises(TypeError):
            models.storage.all([])
            models.storage.all({})
            models.storage.all("")
            models.storage.all(1)
            models.storage.all(None)

    def test_fileStorage_new(self):

        b1 = BaseModel()
        u1 = User()
        s1 = State()
        c1 = City()
        a1 = Amenity()
        p1 = Place()
        r1 = Review()
        models.storage.new(b1)
        models.storage.new(u1)
        models.storage.new(s1)
        models.storage.new(c1)
        models.storage.new(a1)
        models.storage.new(p1)
        models.storage.new(r1)
        self.assertIn("BaseModel." + b1.id, models.storage.all().keys())
        self.assertIn("User." + u1.id, models.storage.all().keys())
        self.assertIn("State." + s1.id, models.storage.all().keys())
        self.assertIn("City." + c1.id, models.storage.all().keys())
        self.assertIn("Amenity." + a1.id, models.storage.all().keys())
        self.assertIn("Place." + p1.id, models.storage.all().keys())
        self.assertIn("Review." + r1.id, models.storage.all().keys())

    def test_fileStorage_new_wrong_args(self):
        with self.assertRaises(AttributeError):
            models.storage.new([])
            models.storage.new({})
            models.storage.new("")
            models.storage.new(1)
            models.storage.new(None)


    def test_fileStorage_new_no_args(self):
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_fileStorage_save(self):
        p = Place()
        models.storage.new(p)
        models.storage.save()

        objs = ""

        with open("file.json", "r") as f:
            self.assertIn(p.id, f.read())
