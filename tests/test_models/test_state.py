#!/usr/bin/python3
"""Test for State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State"""

    def setUp(self):
        """Create State instance for testing"""
        self.state = State()

    def test_name_attribute_present(self):
        """Correct output - State: name class attribute is present"""
        self.assertTrue(hasattr(State, 'name'),
                       "State class missing 'name' attribute")
        self.assertIsInstance(State.name, str),
                            "State.name should be of type str")
        self.assertEqual(self.state.name, "",
                       "State.name should initialize as empty string")

    def test_instance_creation(self):
        """Verify basic instance creation"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsNotNone(self.state.id)


if __name__ == '__main__':
    unittest.main()
