#!/usr/bin/python3
"""Test for State"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State"""

    def setUp(self):
        """Create State instance for testing"""
        self.state = State()

    def test_inheritance(self):
        """1.0 Test if State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test State attributes exist"""
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(self.state.name, "")

    def test_instance_creation(self):
        """3.0 Correct output - State: Instance creation"""
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_save(self):
        """9.0 Test save() updates updated_at"""
        old_updated = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
