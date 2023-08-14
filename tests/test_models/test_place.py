#!/usr/bin/python3
"""
    test from basemodel
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    test place
    """

    def setUp(self):
        self.place = Place()

    def test_creation(self):
        '''
        ensure correct initialization
        '''
        self.assertEqual(self.place.name, '')
