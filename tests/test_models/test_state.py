#!/usr/bin/env python3
"""
    test from basemodel class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    test state
    """

    def setUp(self):
        self.state = State()

    def test_creation(self):
        '''
        ensures correct creation
        '''
        self.assertEqual(self.state.name, '')
