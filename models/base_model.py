#!/usr/bin/python3
"""Defines the BaseModel class with all datetime and serialization fixes"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """Base class with complete datetime and storage integration"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes with UTC timestamps and handles kwargs deserialization"""
        self.id = str(uuid.uuid4())
        now = datetime.now(timezone.utc)
        self.created_at = self.updated_at = now
        
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    if isinstance(value, str):
                        try:
                            value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'
                            ).replace(tzinfo=timezone.utc)
                        except ValueError:
                            value = now
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns formatted string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates timestamp and persists to storage"""
        self.updated_at = datetime.now(timezone.utc)
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns dictionary with proper ISO-8601 timestamps"""
        new_dict = self.__dict__.copy()
        new_dict.pop('_sa_instance_state', None)
        new_dict['__class__'] = self.__class__.__name__
        
        for attr in ('created_at', 'updated_at'):
            if attr in new_dict and isinstance(new_dict[attr], datetime):
                new_dict[attr] = new_dict[attr].isoformat(timespec='microseconds')
        
        return new_dict

    def delete(self):
        """Removes instance from storage"""
        models.storage.delete(self)
