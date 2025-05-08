#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for authentication system
    
    Attributes:
        email (str): empty string
        password (str): empty string
        first_name (str): empty string
        last_name (str): empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
