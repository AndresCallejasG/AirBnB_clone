#!/usr/bin/python3
""" Hbnb project - test Cases - City

"""


import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
from datetime import datetime
import os
from os import path
import pep8


class TestReview(unittest.TestCase):
    """ Test cases for city.py
    """

    @classmethod
    def setUp(self):
        """ Setting up before start all cases
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_pep8(self):
        """ PEP 8 validation
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        pep8_result = pep8_style.check_files(['models/city.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_init(self):
        """ Review all the class and BaseModel attributes
        """
        my_class = City()
        self.assertTrue(hasattr(my_class, "name"))
        self.assertTrue(hasattr(my_class, "state_id"))
        self.assertIsInstance(my_class, City)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_init_kwargs(self):
        """ Review all the class and BaseModel attributes using Kwargs
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "City",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "name": "Betty",
               "state_id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0"}
        my_class = City(**obj)
        self.assertTrue(hasattr(my_class, "name"))
        self.assertTrue(hasattr(my_class, "state_id"))
        self.assertIsInstance(my_class, City)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_heritage(self):
        """ check it is a subclass of BaseModel
        """
        my_class = City()
        self.assertTrue(issubclass(type(my_class), BaseModel))

    def test_str(self):
        """ review format: [<class name>] (<self.id>) <self.__dict__>
        """
        my_class = City()
        string = "[{:s}] ({:s}) {}".format(my_class.__class__.__name__,
                                           my_class.id, my_class.__dict__)
        self.assertEqual(string, my_class.__str__())

    def test_todict(self):
        """ review the dictionary representation of an object
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "City",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "name": "Betty",
               "state_id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0"}
        my_class = City(**obj)
        my_dict = my_class.to_dict()
        for k, v in obj.items():
            self.assertTrue(k in my_dict)
            self.assertEqual(my_dict[k], v)

    def test_update_time(self):
        """ check if updated_at changes
        """
        my_class = City()
        old_updated_time = my_class.updated_at
        my_class.save()
        self.assertNotEqual(old_updated_time, my_class.updated_at)


if __name__ == "__main__":
    unittest.main()
