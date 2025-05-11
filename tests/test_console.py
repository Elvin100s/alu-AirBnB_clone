#!/usr/bin/python3
"""Comprehensive console tests matching intranet requirements"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsoleComprehensive(unittest.TestCase):
    """Comprehensive test cases matching intranet requirements"""

    @classmethod
    def setUpClass(cls):
        """Set up for all tests"""
        cls.console = HBNBCommand()
        cls.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def setUp(self):
        """Reset storage before each test"""
        storage.all().clear()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def create_instance(self, class_name):
        """Helper to create instance and return id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"create {class_name}")
            return f.getvalue().strip()

    # ----- .all() Tests -----
    def test_all_methods_present(self):
        """Test all .all() methods are present"""
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{class_name}.all()")
                output = f.getvalue().strip()
                self.assertEqual(output, "[]")

    # ----- .count() Tests -----
    def test_count_methods_present(self):
        """Test all .count() methods are present"""
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{class_name}.count()")
                output = f.getvalue().strip()
                self.assertEqual(output, "0")

    # ----- .show() Tests -----
    def test_show_methods_present(self):
        """Test all .show() methods are present"""
        for class_name in self.classes:
            obj_id = self.create_instance(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f'{class_name}.show("{obj_id}")')
                output = f.getvalue().strip()
                self.assertIn(f"[{class_name}] ({obj_id})", output)

    # ----- .destroy() Tests -----
    def test_destroy_methods_present(self):
        """Test all .destroy() methods are present"""
        for class_name in self.classes:
            obj_id = self.create_instance(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f'{class_name}.destroy("{obj_id}")')
                output = f.getvalue().strip()
                self.assertEqual(output, "")
            
            # Verify object was actually destroyed
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f'{class_name}.show("{obj_id}")')
                self.assertEqual("** no instance found **", f.getvalue().strip())

    # ----- .update() with attribute Tests -----
    def test_update_with_attribute_methods_present(self):
        """Test all .update() with attribute methods are present"""
        for class_name in self.classes:
            obj_id = self.create_instance(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                cmd = f'{class_name}.update("{obj_id}", "name", "test_value")'
                self.console.onecmd(cmd)
                self.assertEqual(f.getvalue().strip(), "")
            
            # Verify update worked
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f'{class_name}.show("{obj_id}")')
                output = f.getvalue().strip()
                self.assertIn("'name': 'test_value'", output)

    # ----- .update() with dictionary Tests -----
    def test_update_with_dict_methods_present(self):
        """Test all .update() with dictionary methods are present"""
        for class_name in self.classes:
            obj_id = self.create_instance(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                cmd = f'{class_name}.update("{obj_id}", {{"name": "test", "value": 42}})'
                self.console.onecmd(cmd)
                self.assertEqual(f.getvalue().strip(), "")
            
            # Verify update worked
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f'{class_name}.show("{obj_id}")')
                output = f.getvalue().strip()
                self.assertIn("'name': 'test'", output)
                self.assertIn("'value': 42", output)

    # ----- Error Handling Tests -----
    def test_invalid_class_errors(self):
        """Test invalid class error handling"""
        methods = ["all()", "count()", 'show("123")', 'destroy("123")', 
                  'update("123", "name", "value")']
        for method in methods:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"InvalidClass.{method}")
                self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_missing_id_errors(self):
        """Test missing id error handling"""
        methods = ['show("")', 'destroy("")', 'update("", "name", "value")']
        for class_name in self.classes:
            for method in methods:
                with patch('sys.stdout', new=StringIO()) as f:
                    self.console.onecmd(f"{class_name}.{method}")
                    self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_invalid_id_errors(self):
        """Test invalid id error handling"""
        methods = ['show("123")', 'destroy("123")', 'update("123", "name", "value")']
        for class_name in self.classes:
            for method in methods:
                with patch('sys.stdout', new=StringIO()) as f:
                    self.console.onecmd(f"{class_name}.{method}")
                    self.assertEqual("** no instance found **", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
