#!/usr/bin/python3
"""BaseModel"""
import uuid
import datetime

class BaseModel:
    """class attribute"""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.name = kwargs.get('name')
        self.my_number = kwargs.get('my_number')

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'my_number': self.my_number,
            '__class__': self.__class__.__name__,
        }
