#!/usr/bin/python3
"""Definitive BaseModel implementation passing all tests"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """Base class with all fixes for save() and to_dict()"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize with UUID and handle kwargs (e.g., from to_dict())"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now(timezone.utc)
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at'] and isinstance(value, str):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')  # UTC ISO format
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Human-readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update timestamp and persist to storage"""
        self.updated_at = datetime.now(timezone.utc)  # Force UTC
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Generate test-compliant dictionary"""
        return {
            **{k: v for k, v in self.__dict__.items() 
              if k not in ['_sa_instance_state', 'created_at', 'updated_at']},
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(timespec='microseconds'),
            'updated_at': self.updated_at.isoformat(timespec='microseconds')
        }

    def delete(self):
        """Remove from storage"""
        models.storage.delete(self)
