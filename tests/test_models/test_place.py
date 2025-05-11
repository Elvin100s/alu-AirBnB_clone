#!/usr/bin/python3
"""Test for Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place"""

    def setUp(self):
        self.place = Place()

    def test_inheritance(self):
        """Validate inheritance with BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """5.0 Test all required attributes exist"""
        required_attrs = {
            "city_id": "",
            "user_id": "",
            "name": "",
            "description": "",
            "number_rooms": 0,
            "number_bathrooms": 0,
            "max_guest": 0,
            "price_by_night": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "amenity_ids": []
        }
        for attr, default in required_attrs.items():
            self.assertTrue(hasattr(Place, attr))
            self.assertEqual(getattr(self.place, attr), default)

    def test_instance_creation(self):
        """10.0 Correct output - Place: Instance creation"""
        self.assertIsNotNone(self.place.id)
        self.assertTrue(hasattr(self.place, "created_at"))


if __name__ == '__main__':
    unittest.main()
