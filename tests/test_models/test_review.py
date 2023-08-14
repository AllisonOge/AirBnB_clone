#!/usr/bin/python3
"""
    test from base model
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test review
    """

    def setUp(self):
        self.review = Review()

    def test_creation(self):
        '''
        ensures correct creaion
        '''
        self.assertEqual(self.review.text, '')
