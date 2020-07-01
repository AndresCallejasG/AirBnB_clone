#!/usr/bin/python3


""" Hbnb project - test Cases - Place

"""


import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from datetime import datetime
import os
from os import path
import pep8


class TestReview(unittest.TestCase):
    """ Test cases for place.py
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
        pep8_result = pep8_style.check_files(['models/place.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_init(self):
        """ Review all the class and BaseModel attributes
        """
        my_class = Place()
        self.assertTrue(hasattr(my_class, "city_id"))
        self.assertTrue(hasattr(my_class, "user_id"))
        self.assertTrue(hasattr(my_class, "name"))
        self.assertTrue(hasattr(my_class, "description"))
        self.assertTrue(hasattr(my_class, "number_rooms"))
        self.assertTrue(hasattr(my_class, "number_bathrooms"))
        self.assertTrue(hasattr(my_class, "max_guest"))
        self.assertTrue(hasattr(my_class, "price_by_night"))
        self.assertTrue(hasattr(my_class, "latitude"))
        self.assertTrue(hasattr(my_class, "longitude"))
        self.assertTrue(hasattr(my_class, "amenity_ids"))
        self.assertIsInstance(my_class, Place)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_init_kwargs(self):
        """ Review all the class and BaseModel attributes using Kwargs
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "Place",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "city_id": "875398421",
               "user_id": "875930832",
               "name": "BestPlaceEver",
               "description": "text",
               "number_rooms": "4",
               "numbert_bathrooms": "2",
               "max_guest": "3",
               "price_by_night": "90",
               "latitude": "9485734.65",
               "longitude": "478.54",
               "amenity_ids": [""]}
        my_class = Place(**obj)
        self.assertTrue(hasattr(my_class, "city_id"))
        self.assertTrue(hasattr(my_class, "user_id"))
        self.assertTrue(hasattr(my_class, "name"))
        self.assertTrue(hasattr(my_class, "description"))
        self.assertTrue(hasattr(my_class, "number_rooms"))
        self.assertTrue(hasattr(my_class, "number_bathrooms"))
        self.assertTrue(hasattr(my_class, "max_guest"))
        self.assertTrue(hasattr(my_class, "price_by_night"))
        self.assertTrue(hasattr(my_class, "latitude"))
        self.assertTrue(hasattr(my_class, "longitude"))
        self.assertTrue(hasattr(my_class, "amenity_ids"))
        self.assertIsInstance(my_class, Place)
        self.assertTrue(type(my_class.updated_at) is datetime)
        self.assertTrue(type(my_class.created_at) is datetime)

    def test_heritage(self):
        """ check it is a subclass of BaseModel
        """
        my_class = Place()
        self.assertTrue(issubclass(type(my_class), BaseModel))

    def test_str(self):
        """ review format: [<class name>] (<self.id>) <self.__dict__>
        """
        my_class = Place()
        string = "[{:s}] ({:s}) {}".format(my_class.__class__.__name__,
                                           my_class.id, my_class.__dict__)
        self.assertEqual(string, my_class.__str__())

    def test_todict(self):
        """ review the dictionary representation of an object
        """
        obj = {"updated_at": "2020-06-30T23:36:25.091664",
               "created_at": "2020-06-30T23:36:25.091664",
               "__class__": "Place",
               "id": "77822a4e-7aa5-4bb9-871c-5d32f34080e0",
               "city_id": "875398421",
               "user_id": "875930832",
               "name": "BestPlaceEver",
               "description": "text",
               "number_rooms": "4",
               "numbert_bathrooms": "2",
               "max_guest": "3",
               "price_by_night": "90",
               "latitude": "9485734.65",
               "longitude": "478.54",
               "amenity_ids": [""]}
        my_class = Place(**obj)
        my_dict = my_class.to_dict()
        for k, v in obj.items():
            self.assertTrue(k in my_dict)
            self.assertEqual(my_dict[k], v)

    def test_update_time(self):
        """ check if updated_at changes
        """
        my_class = Place()
        old_updated_time = my_class.updated_at
        my_class.save()
        self.assertNotEqual(old_updated_time, my_class.updated_at)


if __name__ == "__main__":
    unittest.main()
