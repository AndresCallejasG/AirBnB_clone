#!/usr/bin/python3

"""
"""

from datetime import datetime
import uuid
import json

class BaseModel:
    """
    """
    def __init__(self):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, 
                                            self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        my_dict = {}
        my_dict["__class__"] = type(self).__name__
        for attr in ["id", "created_at", "updated_at"]:
            if type(attr) is created_at or type(attr) is updated_at:
                my_dict.update({attr: getattr(self, attr)})
        return my_dict

    