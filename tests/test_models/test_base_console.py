#!/usr/bin/python3
"""This module has the test for the base class"""
from tests import reader
import models
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import time
import os
import threading
import signal


class MyTestCase(unittest.TestCase):
    """
    Test console commands
    """

    def setUp(self):
        reader.readed = 0
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def tearDown(self):
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test_basic_io(self):
        reader.readed = 0
        """This is just a example test, don't forget to delete eventually"""
        with patch('sys.stdin', StringIO('Darcy\n')) as stdin,\
                patch('sys.stdout', new_callable=StringIO) as stdout:
            name = input('What is your name? ')
            print('Hello %s' % name)

            assert stdout.getvalue() == 'What is your name? Hello Darcy\n'
            assert stdin.read() == ''  # all input consumed

    def test_quit(self):
        """Test quiting the console"""
        with patch('sys.stdin', StringIO('quit\n')) as\
                stdin, patch('sys.stdout',
                             new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) ')
        with patch('sys.stdin', StringIO('\nquit\n')) as stdin,\
                patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) (hbnb) ')

    def test_help(self):
        """Test help command"""
        with patch('sys.stdin', StringIO('help\n')) as stdin,\
                patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(),
                             '(hbnb) \nDocumented commands (type help <topic>):\n\
========================================\nEOF  all\
  create  destroy  help  quit  show  update\n\n(hbnb) ')

    def test_help_show(self):
        """Test show command"""
        with patch('sys.stdin', StringIO('help show\n')) as stdin,\
                patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '(hbnb) ' +
                             HBNBCommand.do_show.__doc__ + '\n(hbnb) ')

    def test_sintax_error(self):
        """test sintax error message"""
        with patch('sys.stdin', StringIO('<c-d>'))\
                as stdin, patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(),
                             '(hbnb) *** Unknown syntax: <c-d>\n(hbnb) ')

    def test_show_function(self):
        with patch('sys.stdout', new=StringIO()) as stdout:
            HBNBCommand().onecmd('create User')
            User_id = reader.read(stdout)[:-1]
            HBNBCommand().onecmd('show User '+User_id)
            self.assertEqual(reader.read(stdout),
                             str(models.storage.all()['User.'+User_id])+"\n")

    # @patch('console.HBNBCommand')
    # def test_signal_handling(self, mock_print):
        # pid = os.getpid()

        # def trigger_signal():
            # while len(mock_print.mock_calls[0]) < 1:
            # time.sleep(0.2)
            # os.kill(pid, signal.SIGINT)

        # thread = threading.Thread(target=trigger_signal)
        # thread.daemon = True
        # thread.start()

        # # HBNBCommand().cmdloop()
        # # print(mock_print.__dict__)
        # print(mock_print.mock_calls[0])
        # self.assertEqual(mock_print.mock_calls[0], 'Some cleanup')
