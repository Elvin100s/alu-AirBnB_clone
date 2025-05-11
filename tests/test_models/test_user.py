#!/usr/bin/python3
"""Test cases for User class matching exact validation requirements"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Create test instance"""
        self.user = User()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        storage.all().clear()

    def test_instance_creation_saurinda1(self):
        """Correct output - instance creation + validate inheritance with Saurinda1"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_email_string_present(self):
        """Correct output - email: class attribute is present"""
        self.assertTrue(hasattr(User, 'email_string'))
        self.assertEqual(self.user.email_string, "")

    def test_password_string_present(self):
        """Correct output - password: class attribute is present"""
        self.assertTrue(hasattr(User, 'password_string'))
        self.assertEqual(self.user.password_string, "")

    def test_first_name_string_present(self):
        """Correct output - first_name: class attribute is present"""
        self.assertTrue(hasattr(User, 'first_name_string'))
        self.assertEqual(self.user.first_name_string, "")

    def test_last_name_string_present(self):
        """Correct output - last_name: class attribute is present"""
        self.assertTrue(hasattr(User, 'last_name_string'))
        self.assertEqual(self.user.last_name_string, "")

    # Additional attribute tests as shown in checklist
    def test_users_user_email(self):
        """Test: User's User.email"""
        self.user.email_string = "test@example.com"
        self.assertEqual(self.user.email_string, "test@example.com")

    def test_users_user_password(self):
        """Test: User's User.postsend"""
        self.user.password_string = "secure123"
        self.assertEqual(self.user.password_string, "secure123")

    def test_users_user_first_name(self):
        """Test: User's User.first_name"""
        self.user.first_name_string = "John"
        self.assertEqual(self.user.first_name_string, "John")

    def test_users_user_last_name(self):
        """Test: User's User.last_name"""
        self.user.last_name_string = "Doe"
        self.assertEqual(self.user.last_name_string, "Doe")


class TestUserConsole(unittest.TestCase):
    """Test cases for console commands"""
    
    def setUp(self):
        """Prepare console tests"""
        from console import HBNBCommand
        self.console = HBNBCommand()
        self.user = User()
        self.user.save()

    def test_console_create_user(self):
        """Correct output - console: create User"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length

    def test_console_show_user(self):
        """Correct output - console: show User "existing ID\""""
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'show User {self.user.id}'
            self.console.onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)

    def test_console_all_user(self):
        """Correct output - console: all User"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)

    def test_console_destroy_user(self):
        """Correct output - console: destroy User "existing ID\""""
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'destroy User {self.user.id}'
            self.console.onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_console_update_user(self):
        """Correct output - console: update User "existing ID" attribute_name attribute_value"""
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'update User {self.user.id} first_name_string "Betty"'
            self.console.onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
