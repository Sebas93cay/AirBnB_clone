#!/usr/bin/python3
"""This module has the test for the base class"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class MyTestCase(unittest.TestCase):

    def test_basic_io(self):
        """This is just a example test, don't forget to delete eventually"""
        with patch('sys.stdin', StringIO('Darcy\n')) as stdin, patch('sys.stdout', new_callable=StringIO) as stdout:
            name = input('What is your name? ')
            print('Hello %s' % name)

            assert stdout.getvalue() == 'What is your name? Hello Darcy\n'
            assert stdin.read() == ''  # all input consumed

    def test_quit(self):
        """Test quiting the console"""
        with patch('sys.stdin', StringIO('quit\n')) as stdin, patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) ')
        with patch('sys.stdin', StringIO('\nquit\n')) as stdin, patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) (hbnb) ')
    
    def test_help(self):
        with patch('sys.stdin', StringIO('help\n')) as stdin, patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) \nDocumented commands (type help <topic>):\n========================================\nEOF  all  create  destroy  help  quit  show  update\n\n(hbnb) \n') 
