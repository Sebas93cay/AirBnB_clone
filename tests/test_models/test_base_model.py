#!/usr/bin/python3
"""This module has the test for the base class"""
import io
from contextlib import redirect_stdout
from models.base_model import BaseModel
from datetime import datetime
import unittest
from models import storage


class testBaseModel(unittest.TestCase):
    """test for base class"""

    maxDiff = None

    def test_base_model_save(self):
        """test created_at and updated_at instance variables"""
        b1 = BaseModel()
        created1 = b1.created_at
        uptaded1 = b1.updated_at
        b1.save()
        self.assertEqual(created1, b1.created_at)
        self.assertNotEqual(uptaded1, b1.updated_at)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_base_model_save_parameters(self):
        b1 = BaseModel()

        with self.assertRaises(TypeError):
            b1.save(212)
            b1.save("str")
            b1.save({})

    def test_base_model_ids(self):
        """test id instance variable"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.id, str)

    def test_base_model_str(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        r = "[{}] ({}) {}\n".format(type(b1).__name__, b1.id, b1.__dict__)

        with redirect_stdout(io.StringIO()) as f:
            print(b1)
        self.assertEqual(f.getvalue(), r)

    def test_base_model_to_dict(self):
        b1 = BaseModel()
        r = {"__class__": "BaseModel",
             "id": b1.id,
             "created_at": b1.created_at.isoformat(),
             "updated_at": b1.updated_at.isoformat()}
        self.assertDictEqual(b1.to_dict(), r)

    def test_base_model_to_dict_parameters(self):
        b1 = BaseModel()

        with self.assertRaises(TypeError):
            b1.to_dict(212)
            b1.to_dict("str")
            b1.to_dict({})

    def test_base_model_init_copy(self):
        b1 = BaseModel()
        b2 = BaseModel(**b1.to_dict())

        self.assertDictEqual(b1.to_dict(), b2.to_dict())
        self.assertIsNot(b1, b2)

    def test_base_model_storage_all(self):
        b1 = BaseModel()
        # assertEqual(True, storage.all()[
        self.assertIn(b1, storage.all().values())

    def test_base_model_withkey_storage_alll(self):
        b1 = BaseModel(color='green')
        # print(b1)
        # print(storage.all())
        self.assertIn(b1, storage.all().values())
