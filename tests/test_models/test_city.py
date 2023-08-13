#!/usr/bin/env python3
"""
    test from basemodel
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    test city
    """

    def setUp(self):
        self.city = City()

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.city.name, '')
