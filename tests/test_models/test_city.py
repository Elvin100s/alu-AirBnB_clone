#!/usr/bin/python3
"""Test for City"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City"""

    def setUp(self):
        self.city = City()

    def test_inheritance(self):
        """1.0 Validate inheritance with BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """5.0 Test required attributes exist"""
        required_attrs = ["state_id", "name"]
        for attr in required_attrs:
            self.assertTrue(hasattr(City, attr))
            self.assertEqual(getattr(self.city, attr), "")

    def test_instance_creation(self):
        """10.0 Correct output - City: Instance creation"""
        self.assertIsNotNone(self.city.id)
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))


if __name__ == '__main__':
    unittest.main()
