#!/usr/bin/python3
"""
    test from basemodel
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    test amenity
    """

    def setUp(self):
        self.amenity = Amenity()

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.amenity.name, '')
