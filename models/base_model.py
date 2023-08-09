#!/usr/bin/python3
"""
module for base model class
"""
import uuid


class BaseModel:
    """The is the Base model class"""
    def __init__(self):
        """Create an instance of the class"""
        self.id = str(uuid.uuid4())
