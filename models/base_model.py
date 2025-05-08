#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all models in our application."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            time_now = datetime.now()
            if 'created_at' not in kwargs:
                self.created_at = time_now
            if 'updated_at' not in kwargs:
                self.updated_at = time_now
        else:
            self.id = str(uuid.uuid4())
            time_now = datetime.now()
            self.created_at = time_now
            self.updated_at = time_now

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
