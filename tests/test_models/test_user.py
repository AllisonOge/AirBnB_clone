#!/usr/bin/python3
"""
    test for user class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    tests class
    """

    def setUp(self):
        self.user = User()

    def test_creation(self):
        '''
        ensure correct creation
        '''

        data = {'id' : 3,
            'fist_name' : 'Betty',
            'last_name':'Holberton',
            'password':'123',
            'email':'correo@correo',
            }

        self.user = User(**data)
        self.assertEqual(self.user.id, 3)
        self.assertEqual(self.user.first_name, 'Betty')
        self.assertEqual(self.user.first_name, 'Holberton')
        self.assertEqual(self.user.password, '123')
        self.assertEqual(self.user.email, 'correo@correo')
