#!/usr/bin/python3


""" Almost a circle project - test Cases

"""


import unittest
import models
from models.base_model import BaseModel 
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import pep8
from datetime import datetime
import os
from os import path



class TestFile_storage(unittest.TestCase):
    """ Test cases for base_model.py
    """

    @classmethod
    def setUp(self):
        """ Setting up before start all cases
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}
        self.base = BaseModel()


    def tearDown(self):
        """ Executed after each test
        """

    def test_pep8(self):
        """ PEP 8 validation
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        pep8_result = pep8_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.destroy.__doc__)

    def test_init(self):
        """ correct creation if instance
        """
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_all(self):
        """ test of new
        """
        self.assertIsInstance(models.storage.all(), dict)
        with self.assertRaises(TypeError) as error:
            models.storage.all(5)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), msg)

    def test_save(self):
        """
        """
        models.storage.save()
        self.assertTrue(path.exists("file.json"))
        with self.assertRaises(TypeError) as error:
            models.storage.save(5)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), msg)

    def test_new(self):
        """[summary]
        """
        models.storage.new(self.base)
        self.assertFalse(FileStorage._FileStorage__objects == {})    

    def test_reload(self):
        """[summary]
        """
        with self.assertRaises(TypeError) as error:
            models.storage.reload(5)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), msg)

    def test_destroy(self):
        """[summary]
        """
        with self.assertRaises(TypeError) as error:
            models.storage.destroy(5, "3")
        msg = "destroy() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(error.exception), msg)

        with self.assertRaises(KeyError) as error:
            models.storage.destroy("32")

if __name__ == '__main__':
    unittest.main()
