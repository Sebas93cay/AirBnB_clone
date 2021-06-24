#!/usr/bin/python3
"""This module has the test for the base class"""

from models.base_model import BaseModel
import unittest


class testBase(unittest.TestCase):
    """test for base class"""

    def test_dates(self):
        """test created_at and updated_at instance variables"""
        b1 = BaseModel()
        created1 = b1.created_at
        uptaded1 = b1.updated_at
        b1.save()
        self.assertEqual(created1, b1.created_at)
        self.assertNotEqual(uptaded1, b1.updated_at)
