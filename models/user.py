#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user with authentication and personal details
    
    Attributes:
        email (str): User's email address
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade='all, delete-orphan')
        reviews = relationship('Review', backref='user', cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
