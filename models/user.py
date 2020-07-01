#!/usr/bin/pthon3
""" AirBnB Clone project - hbnb
    Command interpreter to manage our AirBnB objects.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ init method
        """
        BaseModel.__init__(self, *args, **kwargs)
