#!/usr/bin/python3
""" AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method
        """
        BaseModel.__init__(self, *args, **kwargs)
