#!/usr/bin/python3

""" AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
"""

from datetime import datetime
import uuid
import json
import models




class BaseModel:
    """ Base Model that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ init method

        Args:
            id (str):  unique id for each BaseModel
            created_at (datetime): current datetime when an instance is created
            updated_at (datetime): current datetime when an instance is created
                and it will be updated every time you change your object
        """

        if kwargs:
            for k in kwargs:
                if k == "__class__":
                    continue
                if k in ["created_at", "updated_at"]:
                    datetime_val = datetime.strptime(kwargs[k],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, datetime_val)
                else:
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())

            time_now = datetime.now()
            self.created_at = time_now
            self.updated_at = time_now
            models.storage.new(self)

    def __str__(self):
        """
            format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """
            saves changes and modify updated_at value
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance and its class name.
        """
        my_dict = {}
        my_dict.update({"__class__": self.__class__.__name__})
        for attr in self.__dict__:
            if attr in ["created_at", "updated_at"]:
                """ datetime isoformat: %Y-%m-%dT%H:%M:%S.%f
                """
                my_dict.update({attr: datetime.isoformat(getattr(self, attr))})
            else:
                my_dict.update({attr: getattr(self, attr)})
        return my_dict
