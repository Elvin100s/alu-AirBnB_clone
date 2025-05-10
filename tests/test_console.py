#!/usr/bin/python3
"""Unit tests for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB command interpreter"""

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()

    def test_prompt(self):
        """Test the custom prompt"""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands", output)
            self.assertIn("EOF", output)
            self.assertIn("help", output)
            self.assertIn("quit", output)

    def test_help_quit(self):
        """Test help quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help quit")
            output = f.getvalue().strip()
            self.assertEqual("Quit command to exit the program", output)

    def test_help_EOF(self):
        """Test help EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help EOF")
            output = f.getvalue().strip()
            self.assertEqual("EOF command to exit the program", output)

    def test_create_BaseModel(self):
        """Test create BaseModel command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_BaseModel(self):
        """Test show BaseModel command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_destroy_BaseModel(self):
        """Test destroy BaseModel command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_all_BaseModel(self):
        """Test all BaseModel command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertEqual("[]", output)

    def test_update_BaseModel(self):
        """Test update BaseModel command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)


if __name__ == '__main__':
    unittest.main()
