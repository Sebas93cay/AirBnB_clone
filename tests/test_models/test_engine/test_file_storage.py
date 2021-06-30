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
        """Delete file.json and set __objects = {} before each test"""
        if os.path.isfile('file.json'):
            os.remove('file.json')
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete file.json and set __objects = {} after each test"""
        if os.path.isfile('file.json'):
            os.remove('file.json')
        FileStorage._FileStorage__objects = {}

    def test_fileStorage_from_models(self):
        """test inicialization of storage var in models"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_fileStorage_init_args(self):
        """test constructor of FileStorage class"""
        with self.assertRaises(TypeError):
            FileStorage("12345")
            FileStorage(1234)
            FileStorage([])
            FileStorage({})
            FileStorage(None)

    def test_fileStorage_attrs(self):
        """check the attributes of FileStorage class"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

        with self.assertRaises(AttributeError):
            models.storage.__file_path
            models.storage.__objects

    def test_fileStorage_all(self):
        """test normal use of function all """
        self.assertEqual(type(models.storage.all()), dict)
        self.assertEqual(len(models.storage.all()), 0)
        models.storage.new(BaseModel())
        self.assertEqual(len(models.storage.all()), 1)

    def test_fileStorage_all_args(self):
        """test arguments of function all"""
        with self.assertRaises(TypeError):
            models.storage.all([])
            models.storage.all({})
            models.storage.all("")
            models.storage.all(1)
            models.storage.all(None)

    def test_fileStorage_new(self):
        """test normal use of function new"""
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
        """test function new without invalid arguments"""
        with self.assertRaises(AttributeError):
            models.storage.new([])
            models.storage.new({})
            models.storage.new("")
            models.storage.new(1)
            models.storage.new(Place(), 1)
            models.storage.new(None)

    def test_fileStorage_new_no_args(self):
        """test function new without arguments"""
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_fileStorage_save(self):
        """test normal use of function save"""
        p = Place()
        b = BaseModel()
        models.storage.new(p)
        models.storage.new(b)
        models.storage.save()

        with open("file.json", "r") as f:
            txt = f.read()
            self.assertIn(p.id, txt)
            self.assertIn(b.id, txt)

    def test_fileStorage_save_args(self):
        """test arguments of function save"""
        with self.assertRaises(TypeError):
            models.storage.save([])
            models.storage.save(User())
            models.storage.save({}, 45)
            models.storage.save("")
            models.storage.save(None)

    def test_fileStorage_reload_withput_file(self):
        """test reload witout file.json"""
        models.storage.reload()
        self.assertEqual(os.path.isfile('file.json'), False)
        self.assertEqual(models.storage.all(), {})


    def test_fileStorage_reload(self):
        """test correct use of reload function"""
        u = User()
        r = Review()
        models.storage.new(u)
        models.storage.new(r)
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()

        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn("Review." + r.id, models.storage.all().keys())

    def test_fileStorage_reload_args(self):
        """test arguments of function reload"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)
            models.storage.reload([])

if __name__ == "__main__":
    unittest.main()
