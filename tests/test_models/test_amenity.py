#!/usr/bin/python3
"""This module has the test for the base class"""
import io
from contextlib import redirect_stdout
from models.amenity import Amenity
from datetime import datetime
import unittest
from models import storage


class testAmenity(unittest.TestCase):
    """test for base class"""

    maxDiff = None

    def test_amenity_save(self):
        """test created_at and updated_at instance variables"""
        b1 = Amenity()
        created1 = b1.created_at
        uptaded1 = b1.updated_at
        b1.save()
        self.assertEqual(created1, b1.created_at)
        self.assertNotEqual(uptaded1, b1.updated_at)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_amenity_save_parameters(self):
        """test save parameter"""
        b1 = Amenity()

        with self.assertRaises(TypeError):
            b1.save(212)
            b1.save("str")
            b1.save({})

    def test_amenity_class_name(self):
        """check the class attr name in Amenity"""
        self.assertEqual(str, type(Amenity.name))

    def test_amenity_ids(self):
        """test id instance variable"""
        b1 = Amenity()
        b2 = Amenity()
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.id, str)

    def test_amenity_str(self):
        """test print represtation of base model"""
        b1 = Amenity()
        b1.name = "Holberton"
        b1.my_number = 89
        r = "[{}] ({}) {}\n".format(type(b1).__name__, b1.id, b1.__dict__)

        with redirect_stdout(io.StringIO()) as f:
            print(b1)
        self.assertEqual(f.getvalue(), r)

    def test_amenity_to_dict(self):
        """test base model to dict method"""
        b1 = Amenity()
        r = {"__class__": "Amenity",
             "id": b1.id,
             "created_at": b1.created_at.isoformat(),
             "updated_at": b1.updated_at.isoformat()}
        self.assertDictEqual(b1.to_dict(), r)

    def test_amenity_to_dict_parameters(self):
        """test base TypeError in to_dict method"""
        b1 = Amenity()

        with self.assertRaises(TypeError):
            b1.to_dict(212)
            b1.to_dict("str")
            b1.to_dict({})

    def test_amenity_init_copy(self):
        """test base model equal object from dictionary"""
        b1 = Amenity()
        b2 = Amenity(**b1.to_dict())

        self.assertDictEqual(b1.to_dict(), b2.to_dict())
        self.assertIsNot(b1, b2)

    def test_amenity_storage_all(self):
        """test save object in storate"""
        b1 = Amenity()
        # assertEqual(True, storage.all()[
        self.assertIn(b1, storage.all().values())

    def test_amenity_withkey_storage_alll(self):
        """test save object to storage"""
        b1 = Amenity(color='green')
        # print(b1)
        # print(storage.all())
        self.assertIn(b1, storage.all().values())
