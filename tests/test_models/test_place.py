#!/usr/bin/python3
"""This module has the test for the base class"""
import io
from contextlib import redirect_stdout
from models.place import Place
from datetime import datetime
import unittest
from models import storage


class testPlace(unittest.TestCase):
    """test for base class"""

    maxDiff = None

    def test_place_save(self):
        """test created_at and updated_at instance variables"""
        b1 = Place()
        created1 = b1.created_at
        uptaded1 = b1.updated_at
        b1.save()
        self.assertEqual(created1, b1.created_at)
        self.assertNotEqual(uptaded1, b1.updated_at)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_place_save_parameters(self):
        """test save parameter"""
        b1 = Place()

        with self.assertRaises(TypeError):
            b1.save(212)
            b1.save("str")
            b1.save({})

    def test_place_class_city_id(self):
        """check the class attr city_id Place"""
        self.assertEqual(str, type(Place.city_id))

    def test_place_class_user_id(self):
        """check the class attr user_id in Place"""
        self.assertEqual(str, type(Place.user_id))

    def test_place_class_name(self):
        """check the class attr name in Place"""
        self.assertEqual(str, type(Place.name))

    def test_place_class_description(self):
        """check the class attr description in Place"""
        self.assertEqual(str, type(Place.description))

    def test_place_class_number_rooms(self):
        """check the class attr number_rooms in Place"""
        self.assertEqual(int, type(Place.number_rooms))

    def test_place_class_number_bathrooms(self):
        """check the class attr number_bathrooms in Place"""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_place_class_max_guest(self):
        """check the class attr max_guest in Place"""
        self.assertEqual(int, type(Place.max_guest))

    def test_place_class_price_by_night(self):
        """check the class attr price_by_night in Place"""
        self.assertEqual(int, type(Place.price_by_night))

    def test_place_class_latitude(self):
        """check the class attr latitude in Place"""
        self.assertEqual(float, type(Place.latitude))

    def test_place_class_longitude(self):
        """check the class attr longitude in Place"""
        self.assertEqual(float, type(Place.longitude))

    def test_place_class_name(self):
        """check the class attr amenity_ids in Place"""
        self.assertEqual(list, type(Place.amenity_ids))

    def test_place_ids(self):
        """test id instance variable"""
        b1 = Place()
        b2 = Place()
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.id, str)

    def test_place_str(self):
        """test print represtation of base model"""
        b1 = Place()
        b1.name = "Holberton"
        b1.my_number = 89
        r = "[{}] ({}) {}\n".format(type(b1).__name__, b1.id, b1.__dict__)

        with redirect_stdout(io.StringIO()) as f:
            print(b1)
        self.assertEqual(f.getvalue(), r)

    def test_place_to_dict(self):
        """test base model to dict method"""
        b1 = Place()
        r = {"__class__": "Place",
             "id": b1.id,
             "created_at": b1.created_at.isoformat(),
             "updated_at": b1.updated_at.isoformat()}
        self.assertDictEqual(b1.to_dict(), r)

    def test_place_to_dict_parameters(self):
        """test base TypeError in to_dict method"""
        b1 = Place()

        with self.assertRaises(TypeError):
            b1.to_dict(212)
            b1.to_dict("str")
            b1.to_dict({})

    def test_place_init_copy(self):
        """test base model equal object from dictionary"""
        b1 = Place()
        b2 = Place(**b1.to_dict())

        self.assertDictEqual(b1.to_dict(), b2.to_dict())
        self.assertIsNot(b1, b2)

    def test_place_storage_all(self):
        """test save object in storate"""
        b1 = Place()
        # assertEqual(True, storage.all()[
        self.assertIn(b1, storage.all().values())

    def test_place_withkey_storage_alll(self):
        """test save object to storage"""
        b1 = Place(color='green')
        # print(b1)
        # print(storage.all())
        self.assertIn(b1, storage.all().values())
