#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """user information"""

    email = ""
    passward = ""
    first_name = ""
    last_name = ""
