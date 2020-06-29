#!/usr/bin/python3

"""AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {}
        for k in self.__objects:
            my_dict.update({k: self.__objects[k].to_dict()})
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(my_dict))

    def reload(self):
        """deserializes the JSON file to __objects
        """
        dict_ = {}
        try:
            with open(self.__file_path, "r") as f:
                dict_ = json.loads(f.read())
                for k, v in dict_.items():
                    class_name = k.split(".")
                    self.__objects[k] = eval(class_name[0])(**v)
        except FileNotFoundError:
            pass

    def destroy(self, key):
        """ deletes an instance from __objects

        Args:
            key (string): <obj class name>.id

            if given key doesn’t exist in dictionary
            it will throw KeyError
        """
        self.__objects.pop(key)
