#!/usr/bin/python3
"""
module for testing file storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the file storage class"""
    def setUp(self):
        """Set up the test"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")

    def tearDown(self):
        """Tear down the test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_storage(self):
        """Test the file storage class"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertEqual(storage._FileStorage__objects, {})

    def test_all(self):
        """Test the all method of the file storage class"""
        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new_one(self):
        """Test the new method of the file storage class with one object"""
        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new_two(self):
        """Test the new method of the file storage class with two objects"""
        storage = FileStorage()
        base = BaseModel()
        base2 = BaseModel()
        storage.new(base)
        storage.new(base2)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_save(self):
        """Test the save method of the file storage class"""
        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertTrue(len(f.read()) > 0)
            self.assertTrue('"BaseModel.' + base.id + '"' in f.read())

    def test_reload(self):
        """Test the reload method of the file storage class"""
        storage = FileStorage()
        self.assertEqual(storage.all(), {})
        base = BaseModel()
        base2 = BaseModel()
        storage.new(base)
        storage.new(base2)
        storage_objects = storage.all()
        storage.save()
        del storage
        storage = FileStorage()
        storage.reload()
        for k, _ in storage_objects.items():
            self.assertTrue(k in storage.all())
