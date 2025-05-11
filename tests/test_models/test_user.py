#!/usr/bin/python3
"""Test cases for User class"""
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

    def test_inheritance(self):
        """Test User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test default attributes exist and are empty strings"""
        attrs = ["email", "password", "first_name", "last_name"]
        for attr in attrs:
            self.assertTrue(hasattr(User, attr))
            self.assertEqual(getattr(self.user, attr), "")

    def test_attribute_assignment(self):
        """Test attribute assignment works correctly"""
        test_values = {
            "email": "test@example.com",
            "password": "secure123",
            "first_name": "John",
            "last_name": "Doe"
        }
        for attr, value in test_values.items():
            setattr(self.user, attr, value)
            self.assertEqual(getattr(self.user, attr), value)

    def test_storage_integration(self):
        """Test User is properly saved to storage"""
        self.user.email = "save@test.com"
        self.user.save()
        key = f"User.{self.user.id}"
        self.assertIn(key, storage.all())
        loaded = storage.all()[key]
        self.assertEqual(loaded.email, "save@test.com")


if __name__ == '__main__':
    unittest.main()
