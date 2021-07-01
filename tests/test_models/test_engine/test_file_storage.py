#!/usr/bin/python3
""" Unittest for FileStorage class.
"""
import os
import pep8
import json
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
class TestFileStorage(unittest.TestCase):
    """"Class to add Unittest for FileStorage class.
        Instance.
    """
    def test_intance_type(self):
        """Check type of an object."""
        fs = FileStorage()
        self.assertEqual(FileStorage, type(fs))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
    def test_permissions(self):
        """Check read-write-execute permisions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)
class TestFileStorage_Attributes(unittest.TestCase):
    """Class to add Unittest for FileStorage class.
       Attributes.
    """
    def testFS_objects(self):
        """Check __objects attribute."""
        fs = FileStorage()
        self.assertEqual(dict, type(fs.all()))
    @unittest.skip('Unknow work')
    def test_FS_empty_objects(self):
        """Check empty __objects attribute."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        fs = FileStorage()
        fs.reload()
        empty = {}
        self.assertEqual(empty, fs.all())
class TestFileStorage_all(unittest.TestCase):
    """Class to add Unittest for FileStorage class.
       all() method.
    """
    def test_all(self):
        """Check the type of __objects attribute.
        """
        ob = FileStorage()
        my_dict = ob.all()
        self.assertEqual(dict, type(my_dict))
        self.assertEqual(dict, type(storage.all()))
class TestFileStorage_new(unittest.TestCase):
    """Class to add Unittest for FileStorage class.
       new() method.
    """
    def test_new(self):
        """Check new() method"""
        b = BaseModel(id="b-new")
        storage.new(b)
        objects_dict = storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        self.assertTrue(b_key in keys)
class TestFileStorage_save(unittest.TestCase):
    """Class to add Unittest for FileStorage class.
       save() method.
    """
    def test_save(self):
        """Check save method."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b_save"
        b = BaseModel(id=id_val, created_at=c_date, updated_at=u_date,)
        storage.new(b)
        storage.save()
        objects_dict = storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        b_dict = b.to_dict()
        with open("file.json", "r") as file:
            json_text = file.read()
        json_dict = eval(json_text)
        self.assertTrue(b_key in json_dict.keys())
        self.assertEqual(json_dict[b_key], b_dict)
class TestFileStorage_reload(unittest.TestCase):
    """Class to add Unittest for FileStorage class.
       reload() method.
    """
    def test_reload(self):
        """Check reload method."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        b_key = "BaseModel.b_reaload"
        b_dict = {'__class__': 'BaseModel',
                  'id': 'b_reaload',
                  'name': "Holberton"
                  }
        json_dict = {b_key: b_dict}
        with open("file.json", "w") as file:
            json.dump(json_dict, file)
        storage.reload()
        object_dict = storage.all()
        self.assertTrue(b_key in object_dict.keys())
        self.assertEqual(object_dict[b_key].name, "Holberton")
class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")
class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)
    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)
