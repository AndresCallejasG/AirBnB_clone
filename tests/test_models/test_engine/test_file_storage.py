#!/usr/bin/python3


""" Almost a circle project - test Cases

"""


import unittest
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
import os.path
from os import path



class TestFile_storage(unittest.TestCase):
    """ Test cases for base_model.py
    """
    @classmethod
    def setUp(cls):
        """ Setting up before start all cases
        """

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

    def test_init(self):
        """ correct creation if instance
        """
        storage = FileStorage()
        storage = FileStorage
        storage.my_number = 89
        self.assertIsInstance(storage, FileStorage)
        self.assertTrue(type(storage.updated_at) is datetime)
        self.assertEqual(storage.name, "Holberton")

    def test_all(self):
        """ test of new
        """
        self.assertEqual(len(self.storge.all()))

    def tets_save(self):
        """
        """
        self.assertIsInstance(models.storage.all(), my_dict)

if __name__ == '__main__':
    unittest.main()
