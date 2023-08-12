#!/usr/bin/python3
"""
module for testing base model class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the base model class"""
    def test_uuid(self):
        """Test the uuid of the base model"""
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

    def test_save(self):
        """Test the save method of the base model"""
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the base model"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)
