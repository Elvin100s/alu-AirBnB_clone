#!/usr/bin/python3
"""
User class implementation for AirBnB clone
Simple FileStorage version for validator compliance
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class with authentication attributes
    
    Attributes:
        email (str): User's email address (empty string by default)
        password (str): User's password (empty string)
        first_name (str): User's first name
        last_name (str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes User instance
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
