#!/usr/bin/python3
"""Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class with public attributes place_id, user_id, and text"""
    place_id = ""
    user_id = ""
    text = ""
