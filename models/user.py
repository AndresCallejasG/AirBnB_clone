#!/usr/bin/pthon3


from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        """
        BaseModel.__init__(self, *args, **kwargs)
