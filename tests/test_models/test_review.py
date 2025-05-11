#!/usr/bin/python3
"""Test for Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review"""

    def setUp(self):
        self.review = Review()

    def test_inheritance(self):
        """7.0 Validate inheritance with BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test required attributes exist"""
        required_attrs = ["place_id", "user_id", "text"]
        for attr in required_attrs:
            self.assertTrue(hasattr(Review, attr))
            self.assertEqual(getattr(self.review, attr), "")

    def test_instance_creation(self):
        """3.0 Correct output - Review: Instance creation"""
        self.assertIsNotNone(self.review.id)
        self.assertTrue(hasattr(self.review, "created_at"))


if __name__ == '__main__':
    unittest.main()
