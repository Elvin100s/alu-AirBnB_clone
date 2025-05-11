#!/usr/bin/python3
"""Test for Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""

    def setUp(self):
        self.amenity = Amenity()

    def test_inheritance(self):
        """6.0 Validate inheritance with BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """4.0 & 8.0 Test attributes exist"""
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertEqual(self.amenity.name, "")
        self.assertTrue(hasattr(Amenity, "laws"))  # 8.0 requirement
        self.assertEqual(self.amenity.laws, "")

    def test_instance_creation(self):
        """4.0 Correct output - Amenity: Instance creation"""
        self.assertIsNotNone(self.amenity.id)
        self.assertTrue(hasattr(self.amenity, "created_at"))


if __name__ == '__main__':
    unittest.main()
