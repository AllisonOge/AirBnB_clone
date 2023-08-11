#!/usr/bin/python3
"""
test module for testing the console one-line program commands
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """test Console class"""
    def test_EOF(self):
        """test the end-of-file condition"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("\n", f.getvalue()) # no output

    def test_quit(self):
        """test the quit command"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_help(self):
        """test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())
